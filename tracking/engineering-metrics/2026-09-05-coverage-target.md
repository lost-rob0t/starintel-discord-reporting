# Engineering metrics snapshot: coverage target

No branch-coverage percentage is being claimed in this snapshot. The current work is to add instrumented coverage gates and publish measured values only after those gates run.

Target:

- 100% reachable branch coverage across maintained code.
- No guessed percentages.
- No denominator gaming by silently excluding maintained branches.
- Publish exact uncovered branches/paths after measurement.

Planned instrumentation examples:

- Zara / Python: coverage.py branch measurement and pytest integration.
- prolog-rlm / SWI-Prolog: native `library(prolog_coverage)` instrumentation.
- Other runtimes: native or ecosystem-standard coverage tooling appropriate to the language.

Public tooling references:

- https://coverage.readthedocs.io/en/latest/branch.html
- https://www.swi-prolog.org/pldoc/man?section=coverage

Current execution evidence kept separate from coverage:

- prolog-rlm repository-recorded gate: 1,218 / 1,218 tests across 98 suites.
- deterministic benchmark: 16 / 16.

The next metrics update should replace placeholders with actual measured line/branch/clause/path coverage and remaining uncovered branches.
