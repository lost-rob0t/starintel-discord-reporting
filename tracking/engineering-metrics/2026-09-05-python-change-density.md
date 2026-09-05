# Engineering metrics snapshot: same-language Python change-density example

This deliberately rough normalization compares Zara and Simon Willison's `llm` because both use Python in their core package.

Inputs:

- Zara: 427 commits in the exact 7-day window; 129 Python files under `zara/`.
- simonw/llm: 9 commits in the exact 7-day window; 18 Python files under `llm/`.

Derived values:

- Zara source-file footprint / llm source-file footprint: `129 / 18 = 7.17x`.
- Zara commit count / llm commit count: `427 / 9 = 47.44x`.
- Zara commits per 100 core Python files: `427 / 129 * 100 = 331.0`.
- llm commits per 100 core Python files: `9 / 18 * 100 = 50.0`.
- Relative normalized cadence: `331.0 / 50.0 = 6.62x`.

Public repositories:

- https://github.com/lost-rob0t/zara
- https://github.com/simonw/llm

Caveat: file count is not LOC, and commit count is not productivity. This is an illustrative normalization of observed integration cadence only.
