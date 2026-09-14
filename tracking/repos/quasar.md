# lost-rob0t/quasar

- generated: `2026-09-14T05:05:03Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`44f977cdecb91d78cd77e35cb287503c135dee50`](https://github.com/lost-rob0t/quasar/commit/44f977cdecb91d78cd77e35cb287503c135dee50)
- head date: `2026-09-06T19:48:04Z`
- head subject: Merge hosted Common Lisp runtime

## Git log, last 14 days

```text
2026-09-06 44f977cdecb91d78cd77e35cb287503c135dee50 Merge hosted Common Lisp runtime
2026-09-06 cb55fdf24505c1edfd226db6c3cbcfbb0af1d22b build: package the hosted Common Lisp runtime
2026-09-06 b2839355a40a006b33f0b203032fe0bfc4d461d5 build: publish web-dist package for the standalone web edition (#70)
2026-08-31 ffd3f903d21abd4adec83b7d47230dc02df922c8 ci: remove software-rendered graph benchmark
2026-08-31 cc88bc9f71fc60deb78c6106ca2731aa2043b692 benchmark: show graph performance tier
2026-08-31 382eb54960ef647771735e33ab3454a1b3dd8f5a perf: hide labels during viewport motion
2026-08-31 9a508007b84b56487feb52c40e9d025dd02a23f5 test: cover graph performance tiers
2026-08-31 363d15d161648bb9c3ed7511d1d1754b9549493d benchmark: measure completed viewport renders
2026-08-31 7577079c56453a11878a2b9379341a9e18d38148 perf: switch graph LOD tiers at runtime
2026-08-31 cb9f03a41bd0f60ed8dfc5b51faefe0c7d9440ec perf: apply LOD styles through runtime tiers
2026-08-31 569d14468ae59c9f8e8d7e47f822419269928769 perf: add graph performance tiers
2026-08-31 8944caec5aa2ac049d15ab813c60c5fa9cb55a71 perf: prefer responsive viewport rendering
2026-08-31 303670be98c587425dab70b20e5713b83d31a36f perf: add high-count graph rendering LOD
2026-08-31 6672151ef84885d3b64a9985856b1ba819e67634 ci: remove misleading software WebGL benchmark
2026-08-31 72c4904f8287bd6347009d025631e1374948ef85 ci: create benchmark directory in main worktree
2026-08-31 02cbc7c46b403dde245be9c3b4b6444dd2337741 ci: shorten renderer benchmark sweep for CI
2026-08-31 0ab9ec04ab051c898bbe9bc9f65637a100df6454 ci: add branch-only graph renderer benchmark
2026-08-31 7861b02f51f63ca74c4c063c3e817ae151c7af80 ci: benchmark WebGL branch against main
2026-08-31 a8fef99f2cb9d4e36663a7c4b45dcc26d50c658b benchmark: exclude renderer fallback from speedup ratios
2026-08-31 2a6278c2687ff9fbac790ffc5bbffd4e474910c6 benchmark: distinguish requested and actual renderer
2026-08-31 07ffadf44afdebbb3d8547d0675b0608af0226ca benchmark: exercise renderer through GraphAdapter boundary
2026-08-31 6006e88e24cfa7e6bd56468735283fcc7ba341a3 ci: restore normal format check
2026-08-31 50802b2bbe7dad076c6c297aafd4b8a192f96dfe style: apply exact Prettier browser benchmark output
2026-08-31 6770a2cec7ecae794fa109e9a304bacc435a6b04 style: apply exact Prettier benchmark output
2026-08-31 8d358d15e4e3ffbf289100b625c193a0485bc562 style: apply exact Prettier renderer output
2026-08-31 f4d14c066a0c04b8885b03bb879d0140cdbf05d2 ci: print exact Prettier patch for GPU slice
2026-08-31 8364cd9279ca2a43d942dc2fc85ed2fc1912ab69 style: wrap renderer benchmark warning
2026-08-31 db8ce1bdfac7c161716c06cc2a5007efa9b827e3 style: match Prettier renderer layout
2026-08-31 8f29e9f48f87a0c631d23a77687774ed9300abe8 style: format browser renderer benchmark
2026-08-31 902a6df16dd4141da6943e3cec3e9ee0e9c9b387 style: format renderer benchmark runner
2026-08-31 9db3d35aae48f83e0e570f5c2dc99845d9b40bd7 style: format GraphAdapter renderer import
2026-08-31 1d4e9dff694ca8c619fd6f9eef065d2e7233ee87 style: format renderer selection module
2026-08-31 6b11802ad9f114ea91e8d73f49566c5d8cafcffc docs: define GPU renderer benchmark gate
2026-08-31 12542c1509fd3b4d341ab1af18f1e9a0fc74c524 test: lock benchmark-gated renderer default
2026-08-31 66a83f7dd1e92ffab7df5991c06e05113c4e3c4e graph: keep Canvas default until benchmark promotion
2026-08-31 e12af9ba4f2dbf9f1af2a8593370d0227b2f3575 chore: preserve frontend dependency versions
2026-08-31 c7b9d423dc7256ad629fb621b78dba4072787c1a benchmark: expose graph renderer sweep at repo root
2026-08-31 2c18566ce52b676bf2e105774efc96b6b2d38fd0 benchmark: report renderer failures without corrupting speedups
2026-08-31 39071cd68dfe24086cca43bd546dda588cd57f53 benchmark: retain failures across large graph sweep
2026-08-31 b5dc4756f1a183a093969f7b29a1a971e40a4382 graph: enable selectable WebGL rendering
2026-08-31 18e688e9857b1103b6a65f8c130a9fa8231e82f4 benchmark: expose renderer sweep command
2026-08-31 5e3647e285ca0a12e94fc2fe1b66c972078250a5 benchmark: compare Canvas and WebGL across graph sizes
2026-08-31 00722e08170543f19d7cc64a17ec769c9829b132 benchmark: add graph renderer browser harness
2026-08-31 3b801522db9d61cb33e1a45e55a7d480a6d3ea60 benchmark: add browser graph renderer sweep
2026-08-31 8c75835a5dabcdc70276e1aa8934580454abfcd1 test: cover graph renderer selection
2026-08-31 3ec774dad4d26f32f11f843d801a6f8c3648fa93 graph: add GPU renderer capability selection
2026-08-31 80553699fa6c9dec227d4ddff629c3ab3a8b8010 chore: remove accidental placeholder
2026-08-31 f0e96b5437ed5fa071a9255988d405322c58fe91 x
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/gpu-benchmark.yml
control-plane/src/configured-main.lisp
flake.lock
flake.nix
frontend/benchmarks/graph-renderer.html
frontend/docs/gpu-renderer-benchmark.md
frontend/package.json
frontend/scripts/benchmark-graph-renderer.mjs
frontend/src/graph/GraphAdapter.js
frontend/src/graph/graph-performance.js
frontend/src/graph/graph-performance.test.js
frontend/src/graph/graph-renderer.js
frontend/src/graph/graph-renderer.test.js
frontend/src/graph/renderer-benchmark.js
frontend/src/lib/graph-style.js
noop
package-lock.json
package.json
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/gpu-benchmark.yml
flake.nix
frontend/scripts/benchmark-graph-renderer.mjs
```
