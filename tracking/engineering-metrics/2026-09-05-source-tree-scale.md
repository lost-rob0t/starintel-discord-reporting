# Engineering metrics snapshot: source-tree scale

Method: GitHub-indexed primary-language source-file counts in each project's main implementation tree. These are rough scale proxies, not LOC measurements.

| Project | Main implementation tree | Primary-language files |
| --- | --- | ---: |
| simonw/llm | `llm/` Python | 18 |
| lost-rob0t/prolog-rlm | `prolog/` Prolog | 88 |
| lost-rob0t/zara | `zara/` Python | 129 |
| nim-lang/nimony | `src/` Nim | 216 |
| astral-sh/uv | `crates/` Rust | 563 |
| zed-industries/zed | `crates/` Rust | 2,108 |
| microsoft/vscode | `src/` TypeScript | 9,824 |

Public repositories:

- https://github.com/simonw/llm
- https://github.com/lost-rob0t/prolog-rlm
- https://github.com/lost-rob0t/zara
- https://github.com/nim-lang/nimony
- https://github.com/astral-sh/uv
- https://github.com/zed-industries/zed
- https://github.com/microsoft/vscode

Caveat: one source file may contain tens or thousands of lines, so this statistic should not be interpreted as LOC, complexity, or engineering effort.
