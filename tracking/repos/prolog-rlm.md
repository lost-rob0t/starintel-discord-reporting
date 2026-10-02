# lost-rob0t/prolog-rlm

- generated: `2026-10-02T12:41:58Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`2596e3f7155a543026adde461a11326c60e1a756`](https://github.com/lost-rob0t/prolog-rlm/commit/2596e3f7155a543026adde461a11326c60e1a756)
- head date: `2026-09-22T23:09:50-04:00`
- head subject: feat(experts): strange-loop KB + canonical expert flow runtime (#507)

## Git log, last 14 days

```text
2026-09-22 2596e3f7155a543026adde461a11326c60e1a756 feat(experts): strange-loop KB + canonical expert flow runtime (#507)
2026-09-20 4715b5ee53d0e7a26c55705ea85c0d16c3916504 feat(style): add generic zero-model overlay resolver runtime
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
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/style-overlay-contract.yml
.github/workflows/tree-sitter.yml
bin/prolog-rlm-zara.pl
docs/common-lisp-adapter.md
docs/zara-runtime.md
flake.nix
lisp/bridge.lisp
lisp/package.lisp
lisp/prolog-rlm-cl.asd
lisp/symbolic-tools.lisp
prolog/adaptors/rlm_common_lisp_bridge.pl
prolog/rlm.pl
prolog/rlm_completion.pl
prolog/rlm_expert.pl
prolog/rlm_expert_graph.pl
prolog/rlm_strange_loop.pl
prolog/rlm_style_overlay.pl
prolog/rlm_symbolic_tool.pl
prolog/rlm_zara_runtime.pl
test/common_lisp_adapter_smoke.lisp
test/deterministic_corpus.pl
test/load_all.pl
test/rlm_completion_stream_test.pl
test/rlm_expert_graph_test.pl
test/rlm_expert_test.pl
test/rlm_strange_loop_test.pl
test/rlm_symbolic_tool_test.pl
test/rlm_zara_runtime_test.pl
test/run_style_overlay_contract.pl
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/style-overlay-contract.yml
.github/workflows/tree-sitter.yml
flake.nix
lisp/prolog-rlm-cl.asd
test/common_lisp_adapter_smoke.lisp
test/deterministic_corpus.pl
test/load_all.pl
test/rlm_completion_stream_test.pl
test/rlm_expert_graph_test.pl
test/rlm_expert_test.pl
test/rlm_strange_loop_test.pl
test/rlm_symbolic_tool_test.pl
test/rlm_zara_runtime_test.pl
test/run_style_overlay_contract.pl
```
