# lost-rob0t/prolog-rlm

- generated: `2026-09-19T17:18:35Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`eba3f90a1d4c0b9342e9e37049f92b178c115c1c`](https://github.com/lost-rob0t/prolog-rlm/commit/eba3f90a1d4c0b9342e9e37049f92b178c115c1c)
- head date: `2026-09-18T21:40:01-04:00`
- head subject: feat: add Common Lisp adapter and symbolic tool harness

## Git log, last 14 days

```text
2026-09-18 eba3f90a1d4c0b9342e9e37049f92b178c115c1c feat: add Common Lisp adapter and symbolic tool harness
2026-09-18 235528ab1420c4803ceb2b011b41f7f4d18887ec Merge pull request #478 from lost-rob0t/fix/zara-runtime-redact-raw-outcomes-1046
2026-09-18 5b7b32946828fdf31c4a4b85baa7a193f5ae6f94 test(runtime): cover malformed outcome redaction
2026-09-18 093659508f29db012043fd99d9d02a04f4990a2d fix(runtime): keep raw outcomes behind Prolog-RLM boundary
2026-09-18 ca7ac96df1e32f1658aa32bae2ba3032fec947c0 test(runtime): reject raw Prolog-RLM outcome leakage
2026-09-18 9c475fe44c24ca58795c6b5cb5e002f2e2decc5e Merge pull request #452 from lost-rob0t/fix/zara-runtime-v1-provenance
2026-09-18 25e656f1c00c368c6b8359144081beff58d8aab0 fix(runtime): project bounded ZARA-RUNTIME provenance
2026-09-18 be996e3f6ea4f0d02ed22483085ed0ab9eeb0c7d test(runtime): lock ZARA-RUNTIME provenance shape
2026-09-18 fa03bb5b48c858b16ec6061d5b49804ee6f29070 feat(runtime): add optional ZARA-RUNTIME/1 sidecar bridge (#448)
2026-09-18 0c7c9d2542a953a9b1202daea558389437f1f853 ci(nix): use supported installer on GitHub runners
2026-09-18 f3edf5b0bfbba185877c134b39f93cbc73fbb577 ci(nix): use supported installer on GitHub runners
2026-09-18 96a1e24bdfafa00b7bd904c29428033474a9e227 test(runtime): cover optional downstream profile advertisement
2026-09-18 525d0c4a71dc26f818d2a16a4d9ec091719d69ee security(runtime): bound advertised profile identifiers
2026-09-18 3ee022ce5872323a7c88c81fca5a0e84fdc80484 build(runtime): package the optional Zara sidecar
2026-09-18 d64e8d9fda0a05f5984443239861aca5e239b830 feat(runtime): allow generic profile advertisement
2026-09-18 73228d3759e2c95340065b727330d2d2dc53e2ac feat(runtime): advertise optional product profiles generically
2026-09-18 227abce776bb89d0f45c58cc9ad57943fcc26fa8 test(runtime): cover request id and wrapped machine faults
2026-09-18 bba4289b161006b49e7f10c235525b41d918c14c fix(runtime): harden request id and wrapped error projection
2026-09-18 22966739e9fa9e0f4d224acebd19769c280e201c fix(runtime): reject control characters in request ids
2026-09-18 628dd763b4eaef8be0e7bf06cc30db4820bd8c5c fix(runtime): use public provider constructor module
2026-09-18 02d290729a148d5c52072f92c0380b033272fb59 docs(runtime): document optional Zara bridge contract
2026-09-18 f6b6575e17197e6773d36a9481be4bbf079b5ea8 test(runtime): register Zara bridge in deterministic corpus
2026-09-18 010b5e9e5922389378ff2001af46773eaad867c1 test(runtime): lock Zara bridge authority and failure contracts
2026-09-18 0e0a8cbfb3ac4b66758d3fef04097d10aba66bea feat(runtime): add loopback Zara sidecar entrypoint
2026-09-18 88a8bebcb351d6da93d58eedf50a81b1d7e54ae6 feat(runtime): add ZARA-RUNTIME/1 Prolog bridge
2026-09-11 51d2530f0e18c84cff860b7c0bf3afcc3c488057 Merge pull request 'fix: #98 review — semantic knowledge review fixes' (#458) from rage/98-semantic-project-knowledge into main
2026-09-11 dfc96cb120c6b33399450acf4d20124905ce0151 ci: install nix via determinate script in the flake workflow
2026-09-11 fbdb276a4da5e8b322b33cc67909e997524e7b12 ci: re-run PR gates after environmental nix-flake runner failure (flake check/build/pack-load/develop-load all pass locally)
2026-09-11 fa41aa355e9fb3b9e248d07d7134792abbc14dd0 fix: #98 review — atomic semantic journal, complete index coherence, incomplete resolution, hydration, host adapters, true project isolation
2026-09-10 d868c110877ff4462ba231f63eef51416623f9ca ci: re-trigger PR gates after paid-lane variable provisioning
2026-09-10 42a7cf64edb60b9976957a73dd4f41a38579eb7e feat: implement #98 semantic project knowledge normalization
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/tree-sitter.yml
.prolog/facts.kb
.prolog/kb/debugging-recipes.pl
.prolog/kb/index.pl
.prolog/kb/project-knowledge-pipeline.pl
.prolog/kb/tree-sitter-ffi.pl
.prolog/verify.pl
README.md
TODO.md
bin/prolog-rlm-zara.pl
c/rlm_tree_sitter_query.c
docs/common-lisp-adapter.md
docs/project-query.md
docs/project-semantic.md
docs/prolog-agent-roadmap.md
docs/zara-runtime.md
flake.nix
lisp/bridge.lisp
lisp/package.lisp
lisp/prolog-rlm-cl.asd
lisp/symbolic-tools.lisp
prolog/adaptors/rlm_common_lisp_bridge.pl
prolog/rlm.pl
prolog/rlm_completion.pl
prolog/rlm_plan_graph.pl
prolog/rlm_project_query.pl
prolog/rlm_project_semantic.pl
prolog/rlm_project_semantic_pack.pl
prolog/rlm_project_semantic_persist.pl
prolog/rlm_project_source.pl
prolog/rlm_symbolic_tool.pl
prolog/rlm_zara_runtime.pl
test/common_lisp_adapter_smoke.lisp
test/deterministic_corpus.pl
test/load_all.pl
test/rlm_completion_stream_test.pl
test/rlm_project_semantic_restart_phase1.pl
test/rlm_project_semantic_restart_phase2.pl
test/rlm_project_semantic_test.pl
test/rlm_symbolic_tool_test.pl
test/rlm_tree_sitter_query_test.pl
test/rlm_zara_runtime_test.pl
test/run_tree_sitter_tests.pl
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/tree-sitter.yml
flake.nix
lisp/prolog-rlm-cl.asd
test/common_lisp_adapter_smoke.lisp
test/deterministic_corpus.pl
test/load_all.pl
test/rlm_completion_stream_test.pl
test/rlm_project_semantic_restart_phase1.pl
test/rlm_project_semantic_restart_phase2.pl
test/rlm_project_semantic_test.pl
test/rlm_symbolic_tool_test.pl
test/rlm_tree_sitter_query_test.pl
test/rlm_zara_runtime_test.pl
test/run_tree_sitter_tests.pl
```
