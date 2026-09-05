# Engineering metrics snapshot: static test-tree density

Method: extension-specific source-file counts in the test tree divided by extension-specific production source-file counts. This is a static repository-layout proxy, not executable coverage and not a runnable test-case count.

| Project | Test-tree files | Production files | Ratio |
| --- | ---: | ---: | ---: |
| lost-rob0t/zara | 154 Python files under `t/` | 129 Python files under `zara/` | 1.19x |
| lost-rob0t/prolog-rlm | 194 Prolog files under `test/` | 88 Prolog files under `prolog/` | 2.20x |
| simonw/llm | 44 files under `tests/` | 18 Python files under `llm/` | 2.44x |
| nim-lang/nimony | 972 Nim files under `tests/` | 216 Nim files under `src/` | 4.50x |

Additional execution evidence for prolog-rlm recorded in repository verification material:

- 1,218 / 1,218 tests passing.
- 98 suites.
- 16 / 16 deterministic benchmark cases.

Public repositories:

- https://github.com/lost-rob0t/zara
- https://github.com/lost-rob0t/prolog-rlm
- https://github.com/simonw/llm
- https://github.com/nim-lang/nimony

Important: 972 test source files does not mean 972 runnable test cases, and 1,218 runnable Prolog tests does not mean 1,218 test files. Different test architectures are intentionally kept separate.
