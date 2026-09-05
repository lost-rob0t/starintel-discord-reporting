# Engineering metrics snapshot: 7-day commit throughput

Window: `2026-08-29T06:31:00Z` through `2026-09-05T06:31:00Z`.

Method: count default-branch commits whose commit timestamp falls inside the exact window. This measures integration/change cadence only. It is not a productivity, headcount, difficulty, or LOC metric.

| Project | 7-day commits | Per day |
| --- | ---: | ---: |
| lost-rob0t/zara | 427 | 61.0 |
| lost-rob0t/prolog-rlm | 129 | 18.4 |
| lost-rob0t/hackmode | 108 | 15.4 |
| lost-rob0t/starintel-auto-research | 68 | 9.7 |
| lost-rob0t/quasar | 45 | 6.4 |
| lost-rob0t/starintel-server | 2 | 0.3 |
| Hot-6 total | 779 | 111.3 |
| microsoft/vscode | 453 | 64.7 |
| zed-industries/zed | 110 | 15.7 |
| astral-sh/uv | 71 | 10.1 |
| simonw/llm | 9 | 1.3 |

Derived comparisons:

- Hot-6 / VS Code: `779 / 453 = 1.72x`.
- Zara / VS Code: `427 / 453 = 94.3%`.
- Zara / Zed: `427 / 110 = 3.88x`.
- prolog-rlm / Zed: `129 / 110 = 1.17x`.
- Hackmode / Zed: `108 / 110 = 98.2%`.
- Zara / simonw/llm: `427 / 9 = 47.44x`.

Public repositories / histories:

- https://github.com/lost-rob0t/zara/commits/master/
- https://github.com/lost-rob0t/prolog-rlm/commits/main/
- https://github.com/lost-rob0t/hackmode/commits/master/
- https://github.com/lost-rob0t/starintel-auto-research/commits/main/
- https://github.com/lost-rob0t/quasar/commits/main/
- https://github.com/lost-rob0t/starintel-server/commits/master/
- https://github.com/microsoft/vscode/commits/main/
- https://github.com/zed-industries/zed/commits/main/
- https://github.com/astral-sh/uv/commits/main/
- https://github.com/simonw/llm/commits/main/
