#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

OPENAI_IMAGE_ENDPOINT = "https://api.openai.com/v1/images/generations"
IMAGE_MODES = {"star-trek-meme", "star-trek-comic"}


def extract_finding(report: str) -> str:
    lines = []
    in_sources = False
    for raw in report.splitlines():
        line = raw.strip()
        if line == "## Sources":
            in_sources = True
            continue
        if in_sources or not line or line.startswith("#") or line.startswith("http"):
            continue
        line = re.sub(r"^[>*-]+\s*", "", line)
        line = re.sub(r"[*_`]", "", line)
        if len(line) >= 24:
            lines.append(line)
    return " ".join(lines[:3])[:900]


def prompt_for(mode: str, finding: str) -> str:
    shared = (
        "Create a square Star Trek parody image for a Discord Auto-Dig shitpost. "
        "Data is always Auto-Dig. Treat Data as the obsessive evidence-checking investigator. "
        "The factual setup comes from this already-verified finding: " + finding + ". "
        "Do not add factual allegations that are not in that setup. "
        "Use a dark black-and-gold StarIntel visual accent where it fits. "
        "Keep any visible text extremely short and readable. No watermark."
    )
    if mode == "star-trek-meme":
        return shared + (
            " Make it a single-image meme. Data has just checked the receipts while the rest of the bridge "
            "looks like they were about to trust the summary. Dry, deadpan punchline."
        )
    if mode == "star-trek-comic":
        return shared + (
            " Make it a short 3-panel comic. Panel 1: somebody presents the claim. "
            "Panel 2: Data/Auto-Dig checks the evidence. Panel 3: deadpan verified result or correction. "
            "One finding only. Do not cram the panels with prose."
        )
    raise ValueError(f"unsupported media mode: {mode}")


def generate_image(mode: str, report: Path, output: Path) -> bool:
    if mode not in IMAGE_MODES:
        return False

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print(f"{mode}: OPENAI_API_KEY missing, posting without image")
        return False

    finding = extract_finding(report.read_text(encoding="utf-8"))
    if not finding:
        print(f"{mode}: no usable finding text, posting without image")
        return False

    payload = json.dumps(
        {
            "model": "gpt-image-1",
            "prompt": prompt_for(mode, finding),
            "size": "1024x1024",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        OPENAI_IMAGE_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "starintel-discord-reporting/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.load(response)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        print(f"{mode}: image generation failed, posting without image: {exc}")
        return False

    item = (data.get("data") or [{}])[0]
    encoded = item.get("b64_json")
    url = item.get("url")
    output.parent.mkdir(parents=True, exist_ok=True)

    if encoded:
        output.write_bytes(base64.b64decode(encoded))
        print(f"generated {output}")
        return True
    if url:
        try:
            with urllib.request.urlopen(url, timeout=120) as response:
                output.write_bytes(response.read())
            print(f"generated {output}")
            return True
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            print(f"{mode}: generated image download failed, posting without image: {exc}")
            return False

    print(f"{mode}: image API returned no image, posting without image")
    return False


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    generate_image(args.mode, args.report, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
