#!/usr/bin/env python3
from __future__ import annotations

import json, os, random, re, urllib.request
from datetime import datetime, timezone
from pathlib import Path

OWNER = "lost-rob0t"
AUTO_DIG = f"{OWNER}/starintel-gpt-auto-dig"
STATE = Path("state/source-state.json")
PENDING_STATE = Path("state/source-state.pending.json")
REPORTS = Path("reports")
REPOS_FILE = Path("config/starintel-repos.txt")
URL_RE = re.compile(r"https://[^\s)>\]}]+")


def gh(path: str):
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "starintel-discord-reporting/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    PENDING_STATE.write_text(json.dumps(s, indent=2, sort_keys=True) + "\n")


def safe_get_file(repo: str, path: str, ref: str) -> str | None:
    try:
        data = gh(f"/repos/{repo}/contents/{path}?ref={ref}")
        import base64
        return base64.b64decode(data.get("content", "")).decode("utf-8", "replace")
    except Exception:
        return None


def extract_findings(text: str) -> list[str]:
    if not text:
        return []
    out = []
    active = False
    for line in text.splitlines():
        if re.match(r"^#{1,3}\s+", line):
            title = line.lstrip("# ").lower()
            active = any(k in title for k in ("finding", "summary", "result", "evidence"))
            continue
        if active and re.match(r"^\s*[-*]\s+", line):
            item = re.sub(r"^\s*[-*]\s+", "", line).strip()
            if 20 <= len(item) <= 420:
                out.append(item)
        if len(out) >= 4:
            break
    if not out:
        for p in re.split(r"\n\s*\n", text):
            p = " ".join(x.strip() for x in p.splitlines() if x.strip() and not x.startswith("#"))
            if 40 <= len(p) <= 420:
                out.append(p)
            if len(out) >= 3:
                break
    return out


def source_urls(text: str) -> list[str]:
    return list(dict.fromkeys(URL_RE.findall(text or "")))[:8]


def latest_repo_head(repo: str):
    meta = gh(f"/repos/{repo}")
    branch = meta["default_branch"]
    if branch not in {"main", "master"}:
        return branch, None
    return branch, gh(f"/repos/{repo}/commits/{branch}")["sha"]


def changed_commits(repo: str, old: str, new: str):
    if old == new:
        return []
    try:
        return gh(f"/repos/{repo}/compare/{old}...{new}").get("commits", [])
    except Exception:
        return []


def merged_pr_for_commit(repo: str, sha: str, branch: str):
    try:
        prs = gh(f"/repos/{repo}/commits/{sha}/pulls")
    except Exception:
        return None
    for pr in prs:
        if pr.get("merged_at") and pr.get("base", {}).get("ref") == branch:
            return pr
    return None


def write_report(channel: str, body: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    directory = REPORTS / channel
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{stamp}-report.md"
    path.write_text(body.rstrip() + "\n")
    return path


def auto_dig_reports(state: dict) -> list[tuple[str, Path, str]]:
    _, head = latest_repo_head(AUTO_DIG)
    if not head:
        return []
    old = state.get("auto_dig_head")
    state["auto_dig_head"] = head
    if not old:
        return []
    readmes = []
    for commit in changed_commits(AUTO_DIG, old, head):
        sha = commit["sha"]
        try:
            files = gh(f"/repos/{AUTO_DIG}/commits/{sha}").get("files", [])
        except Exception:
            continue
        for item in files:
            path = item.get("filename", "")
            if path.startswith("digs/") and path.endswith("/README.md"):
                readmes.append((path, sha))
    seen, items, urls = set(), [], []
    for path, sha in readmes:
        if path in seen:
            continue
        seen.add(path)
        text = safe_get_file(AUTO_DIG, path, head)
        findings = extract_findings(text or "")
        source_path = path.rsplit("/", 1)[0] + "/sources.md"
        source_text = safe_get_file(AUTO_DIG, source_path, head) or ""
        source_list = source_urls(source_text) or source_urls(text or "")
        if len(source_list) < 2 or not findings:
            continue
        items.append((path, findings[:3], sha, source_list[:4]))
        urls.extend(source_list[:4])
    if not items:
        return []

    serious = ["# Auto-Dig findings", "", "## Findings"]
    for path, findings, sha, _ in items[:4]:
        serious.append(f"**{path.split('/')[-2]}**")
        serious.extend(f"- {finding}" for finding in findings)
        serious.append(f"- merged: https://github.com/{AUTO_DIG}/commit/{sha}")
        serious.append("")
    serious += ["## Sources"] + [f"- {url}" for url in list(dict.fromkeys(urls))[:8]]
    serious += ["", "This report was written by AI. Check it yourself.", "Do not trust this report as a source. Don't even trust NSA Spy.", "SIGNED OFF BY: N545PY"]
    serious_path = write_report("auto-dig-findings", "\n".join(serious))

    facts = [finding for _, findings, _, _ in items for finding in findings][:4]
    if random.choice([True, False]):
        body = ["# findings shitposts", ""] + [f">{fact[:300]}" for fact in facts]
        body += [">open the receipts urself", "", "## Sources"]
    else:
        body = ["# findings shitposts", "", "auto-dig found some shit again.", ""]
        body += [fact[:320] for fact in facts]
        body += ["", "dont take my word for it. links are right there.", "", "## Sources"]
    body += [f"- {url}" for url in list(dict.fromkeys(urls))[:6]]
    shitpost_path = write_report("findings-shitposts", "\n".join(body))
    return [("auto-dig-findings", serious_path, "findings"), ("findings-shitposts", shitpost_path, "shitpost")]


def changelog_report(state: dict) -> list[tuple[str, Path, str]]:
    changes = []
    state.setdefault("changelog", {})
    for raw in REPOS_FILE.read_text().splitlines():
        name = raw.strip()
        if not name or name.startswith("#"):
            continue
        repo = name if "/" in name else f"{OWNER}/{name}"
        try:
            branch, head = latest_repo_head(repo)
        except Exception:
            continue
        if not head:
            continue
        old = state["changelog"].get(repo)
        state["changelog"][repo] = head
        if not old:
            continue
        for commit in changed_commits(repo, old, head):
            pr = merged_pr_for_commit(repo, commit["sha"], branch)
            if not pr:
                continue
            changes.append((repo, pr.get("title", "").strip(), commit["sha"], pr.get("number")))
    if not changes:
        return []
    body = ["# StarIntel updates", "", "## Changes"]
    for repo, title, sha, pr_number in changes[:20]:
        body += [f"**{repo.split('/')[-1]}**", f"- {title}", f"- PR #{pr_number}", f"- https://github.com/{repo}/commit/{sha}", ""]
    return [("starintel-updates-changelog", write_report("starintel-updates-changelog", "\n".join(body)), "changelog")]


def main():
    state = load_state()
    created = auto_dig_reports(state) + changelog_report(state)
    save_state(state)
    for channel, path, kind in created:
        print(f"{channel}\t{kind}\t{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
