#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import os
import random
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OWNER = "lost-rob0t"
AUTO_DIG = f"{OWNER}/starintel-gpt-auto-dig"
STATE = Path("state/source-state.json")
PENDING_STATE = Path("state/source-state.pending.json")
REPORTS = Path("reports")
REPOS_FILE = Path("config/starintel-repos.txt")
URL_RE = re.compile(r"https://[^\s)>\]}]+")
STOPWORDS = {
    "about", "after", "again", "against", "being", "between", "could", "found",
    "from", "have", "into", "more", "other", "over", "same", "that", "their",
    "there", "these", "they", "this", "through", "under", "using", "were", "where",
    "which", "while", "with", "would",
}


def gh(path: str):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "starintel-discord-reporting/1.0"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=headers), timeout=30) as response:
        return json.load(response)


def load_state() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_pending_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    PENDING_STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def repo_file(repo: str, path: str, ref: str) -> str | None:
    try:
        data = gh(f"/repos/{repo}/contents/{path}?ref={ref}")
        return base64.b64decode(data.get("content", "")).decode("utf-8", "replace")
    except Exception:
        return None


def fetch_source_text(url: str) -> str:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "starintel-discord-reporting/1.0"})
        with urllib.request.urlopen(request, timeout=15) as response:
            raw = response.read(1_000_000).decode("utf-8", "replace")
        raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.I | re.S)
        return re.sub(r"<[^>]+>", " ", raw).lower()
    except Exception:
        return ""


def corroborated(claim: str, urls: list[str]) -> bool:
    terms = [w.lower() for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]{4,}", claim)]
    terms = [w for w in dict.fromkeys(terms) if w not in STOPWORDS][:12]
    if len(terms) < 3:
        return False
    threshold = max(3, min(5, len(terms) // 2))
    hits = 0
    for url in urls:
        text = fetch_source_text(url)
        if text and sum(term in text for term in terms) >= threshold:
            hits += 1
        if hits >= 2:
            return True
    return False


def extract_findings(text: str) -> list[str]:
    if not text:
        return []
    found, active = [], False
    for line in text.splitlines():
        if re.match(r"^#{1,3}\s+", line):
            active = any(k in line.lower() for k in ("finding", "summary", "result", "evidence"))
            continue
        if active and re.match(r"^\s*[-*]\s+", line):
            item = re.sub(r"^\s*[-*]\s+", "", line).strip()
            if 20 <= len(item) <= 420:
                found.append(item)
        if len(found) >= 4:
            break
    if found:
        return found
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = " ".join(x.strip() for x in paragraph.splitlines() if x.strip() and not x.startswith("#"))
        if 40 <= len(paragraph) <= 420:
            found.append(paragraph)
        if len(found) >= 3:
            break
    return found


def urls(text: str) -> list[str]:
    return list(dict.fromkeys(URL_RE.findall(text or "")))[:8]


def head(repo: str):
    meta = gh(f"/repos/{repo}")
    branch = meta["default_branch"]
    if branch not in {"main", "master"}:
        return branch, None
    return branch, gh(f"/repos/{repo}/commits/{branch}")["sha"]


def commits(repo: str, old: str, new: str) -> list[dict]:
    if old == new:
        return []
    try:
        return gh(f"/repos/{repo}/compare/{old}...{new}").get("commits", [])
    except Exception:
        return []


def merged_pr(repo: str, sha: str, branch: str):
    try:
        candidates = gh(f"/repos/{repo}/commits/{sha}/pulls")
    except Exception:
        return None
    return next((pr for pr in candidates if pr.get("merged_at") and pr.get("base", {}).get("ref") == branch), None)


def write_report(channel: str, body: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    directory = REPORTS / channel
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{stamp}-report.md"
    path.write_text(body.rstrip() + "\n")
    return path


def auto_dig_reports(state: dict) -> list[tuple[str, Path, str]]:
    _, current = head(AUTO_DIG)
    if not current:
        return []
    previous = state.get("auto_dig_head")
    state["auto_dig_head"] = current
    if not previous:
        return []

    changed = []
    for commit in commits(AUTO_DIG, previous, current):
        sha = commit["sha"]
        try:
            files = gh(f"/repos/{AUTO_DIG}/commits/{sha}").get("files", [])
        except Exception:
            continue
        changed.extend((item.get("filename", ""), sha) for item in files if item.get("filename", "").startswith("digs/") and item.get("filename", "").endswith("/README.md"))

    items, all_urls, seen = [], [], set()
    for path, sha in changed:
        if path in seen:
            continue
        seen.add(path)
        text = repo_file(AUTO_DIG, path, current) or ""
        source_path = path.rsplit("/", 1)[0] + "/sources.md"
        source_list = urls(repo_file(AUTO_DIG, source_path, current) or "") or urls(text)
        findings = extract_findings(text)
        if len(source_list) < 2 or not findings:
            continue
        verified = [finding for finding in findings if corroborated(finding, source_list[:4])]
        if not verified:
            continue
        items.append((path, verified[:3], sha, source_list[:4]))
        all_urls.extend(source_list[:4])

    if not items:
        return []

    serious = ["# Auto-Dig findings", "", "## Findings"]
    for path, findings, sha, _ in items[:4]:
        serious += [f"**{path.split('/')[-2]}**", *[f"- {finding}" for finding in findings], f"- merged: https://github.com/{AUTO_DIG}/commit/{sha}", ""]
    serious += ["## Sources", *[f"- {url}" for url in list(dict.fromkeys(all_urls))[:8]], "", "This report was written by AI. Check it yourself.", "Do not trust this report as a source. Don't even trust NSA Spy.", "SIGNED OFF BY: N545PY"]
    serious_path = write_report("auto-dig-findings", "\n".join(serious))

    facts = [finding for _, findings, _, _ in items for finding in findings][:4]
    if random.choice([True, False]):
        shitpost = ["# findings shitposts", "", *[f">{fact[:300]}" for fact in facts], ">open the receipts urself", "", "## Sources"]
    else:
        shitpost = ["# findings shitposts", "", "auto-dig found some shit again.", "", *[fact[:320] for fact in facts], "", "dont take my word for it. links are right there.", "", "## Sources"]
    shitpost += [f"- {url}" for url in list(dict.fromkeys(all_urls))[:6]]
    shitpost_path = write_report("findings-shitposts", "\n".join(shitpost))
    return [("auto-dig-findings", serious_path, "findings"), ("findings-shitposts", shitpost_path, "shitpost")]


def changelog_report(state: dict) -> list[tuple[str, Path, str]]:
    state.setdefault("changelog", {})
    changes = []
    for raw in REPOS_FILE.read_text().splitlines():
        name = raw.strip()
        if not name or name.startswith("#"):
            continue
        repo = name if "/" in name else f"{OWNER}/{name}"
        try:
            branch, current = head(repo)
        except Exception:
            continue
        if not current:
            continue
        previous = state["changelog"].get(repo)
        state["changelog"][repo] = current
        if not previous:
            continue
        for commit in commits(repo, previous, current):
            pr = merged_pr(repo, commit["sha"], branch)
            if pr:
                changes.append((repo, pr.get("title", "").strip(), commit["sha"], pr.get("number")))
    if not changes:
        return []
    body = ["# StarIntel updates", "", "## Changes"]
    for repo, title, sha, number in changes[:20]:
        body += [f"**{repo.split('/')[-1]}**", f"- {title}", f"- PR #{number}", f"- https://github.com/{repo}/commit/{sha}", ""]
    return [("starintel-updates-changelog", write_report("starintel-updates-changelog", "\n".join(body)), "changelog")]


def main() -> int:
    state = load_state()
    created = auto_dig_reports(state) + changelog_report(state)
    save_pending_state(state)
    for channel, path, kind in created:
        print(f"{channel}\t{kind}\t{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
