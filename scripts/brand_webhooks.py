#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import mimetypes
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "discord-identities.json"


def image_data(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def patch_webhook(webhook_url: str, *, name: str, avatar: Path | None) -> None:
    payload: dict[str, str] = {"name": name}
    if avatar is not None and avatar.is_file():
        payload["avatar"] = image_data(avatar)

    request = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "starintel-discord-reporting/1.0",
        },
        method="PATCH",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if not 200 <= response.status < 300:
                raise RuntimeError(f"Discord returned HTTP {response.status}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Discord webhook branding failed with HTTP {exc.code}: {body}") from exc


def main() -> int:
    identities = json.loads(CONFIG.read_text(encoding="utf-8"))
    for channel, identity in identities.items():
        secret_env = identity["secret_env"]
        webhook_url = os.environ.get(secret_env, "").strip()
        if not webhook_url:
            raise RuntimeError(f"missing webhook environment variable: {secret_env}")

        avatar_path = ROOT / identity["avatar"]
        patch_webhook(
            webhook_url,
            name=identity["name"],
            avatar=avatar_path if avatar_path.is_file() else None,
        )
        avatar_status = avatar_path.as_posix() if avatar_path.is_file() else "pending image"
        print(f"branded {channel}: {identity['name']} ({avatar_status})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
