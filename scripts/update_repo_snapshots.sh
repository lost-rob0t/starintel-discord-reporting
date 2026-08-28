#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
CONFIG="$ROOT/config/starintel-repo-tracking.tsv"
OUT="$ROOT/tracking/repos"
CACHE="${XDG_CACHE_HOME:-$HOME/.cache}/starintel-discord-reporting/repos"
SINCE="14 days ago"

command -v gh >/dev/null || { echo "gh is required" >&2; exit 2; }
command -v git >/dev/null || { echo "git is required" >&2; exit 2; }

mkdir -p "$OUT" "$CACHE"
required_failures=()
optional_failures=()

refresh_repo() {
  local repo=$1
  local branch=$2
  local changelog=$3
  local name=${repo##*/}
  local dir="$CACHE/$name"
  local out="$OUT/$name.md"
  local head generated head_date head_subject tmp

  if [[ ! -d "$dir/.git" ]]; then
    rm -rf "$dir"
    if ! gh repo clone "$repo" "$dir" -- --filter=blob:none --no-checkout --quiet; then
      return 1
    fi
  fi

  git -C "$dir" remote set-url origin "https://github.com/$repo.git" || return 1
  git -C "$dir" fetch --quiet --prune origin "$branch" || return 1
  head=$(git -C "$dir" rev-parse "origin/$branch") || return 1
  generated=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  head_date=$(git -C "$dir" show -s --format=%cI "$head") || return 1
  head_subject=$(git -C "$dir" show -s --format=%s "$head") || return 1

  tmp=$(mktemp)
  {
    printf '# %s\n\n' "$repo"
    printf -- '- generated: `%s`\n' "$generated"
    printf -- '- canonical branch: `%s`\n' "$branch"
    printf -- '- changelog eligible: `%s`\n' "$changelog"
    printf -- '- head: [`%s`](https://github.com/%s/commit/%s)\n' "$head" "$repo" "$head"
    printf -- '- head date: `%s`\n' "$head_date"
    printf -- '- head subject: %s\n\n' "$head_subject"

    printf '## Git log, last 14 days\n\n```text\n'
    git -C "$dir" log "origin/$branch" --since="$SINCE" --date=short --pretty=format:'%ad %H %s' || true
    printf '\n```\n\n'

    printf '## Repository paths changed, last 14 days\n\n```text\n'
    git -C "$dir" log "origin/$branch" --since="$SINCE" --name-only --pretty=format: \
      | sed '/^$/d' | sort -u || true
    printf '```\n\n'

    printf '## Test and CI paths touched, last 14 days\n\n```text\n'
    git -C "$dir" log "origin/$branch" --since="$SINCE" --name-only --pretty=format: \
      | sed '/^$/d' \
      | grep -Ei '(^|/)(t|test|tests|spec|ci|scripts)(/|$)|\.github/workflows|stack-test|flake\.nix|\.asd$' \
      | sort -u || true
    printf '```\n'
  } > "$tmp"

  mv "$tmp" "$out"
  echo "updated $out"
}

while IFS=$'\t' read -r repo branch changelog; do
  [[ "$repo" == "repo" || -z "$repo" ]] && continue
  if ! refresh_repo "$repo" "$branch" "$changelog"; then
    if [[ "$changelog" == "yes" ]]; then
      required_failures+=("$repo")
      echo "required snapshot refresh failed for $repo; continuing with remaining repositories" >&2
    else
      optional_failures+=("$repo")
      echo "optional snapshot refresh failed for $repo; continuing with remaining repositories" >&2
    fi
  fi
done < "$CONFIG"

{
  printf '# StarIntel repository snapshots\n\n'
  printf 'Generated from canonical branches by `scripts/update_repo_snapshots.sh`. These are evidence caches, not claims of test success.\n\n'
  for file in "$OUT"/*.md; do
    base=$(basename "$file")
    [[ "$base" == "index.md" ]] && continue
    repo=$(sed -n '1s/^# //p' "$file")
    head=$(sed -n 's/^- head: \[`\([^`]*\)`.*/\1/p' "$file")
    printf -- '- [%s](./%s) `%s`\n' "$repo" "$base" "${head:0:12}"
  done | sort
} > "$OUT/index.md"

if (( ${#optional_failures[@]} > 0 )); then
  printf 'optional repo snapshots unavailable:' >&2
  printf ' %s' "${optional_failures[@]}" >&2
  printf '\n' >&2
fi

if (( ${#required_failures[@]} > 0 )); then
  printf 'required changelog snapshots partially refreshed; inaccessible/failed repositories:' >&2
  printf ' %s' "${required_failures[@]}" >&2
  printf '\n' >&2
  exit 1
fi

echo "repo snapshots refreshed"
