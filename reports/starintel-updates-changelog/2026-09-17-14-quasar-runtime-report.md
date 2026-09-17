# Quasar: separate deployable web and Common Lisp runtime artifacts

## FOLLOW-UP

This adds the concrete runtime-build and startup-validation implementation behind the earlier packaging summary.

September 17, 2026. Quasar's new packaging work makes the difference between serving the interface and running its control plane explicit. The native Android client is a separate application and receives its own platform post.

## Changes

### The static web edition has a defined output

The web-dist package produces the frontend's production bundle as a root-hosted static application. It packages browser-facing files without pretending those files contain the Common Lisp control plane.

This gives deployment a named artifact instead of requiring someone to find and copy an arbitrary build directory. A successful page load proves that the assets were served; it does not establish that runtime-backed operations are available. Keeping that distinction visible makes a hosted interface easier to deploy and diagnose honestly.

### The hosted runtime is packaged as an executable Lisp image

The new server package assembles the control, StarLang and web systems, includes the built frontend and saves an executable SBCL image. Its build graph includes the necessary native/runtime dependencies and authentication-host integration.

A running development REPL that happens to contain the right libraries is not a reproducible deployment artifact. This change makes the assembly part of the build definition. The named server output exists alongside the static output rather than silently changing what the static package means.

Startup also accepts explicit listener-host, HTTP-port, WebSocket-port and storage-path configuration. Port values are parsed as integers and validated against the TCP port range. Invalid configuration fails before it can become a malformed listener request.

### Choose the artifact that matches the intended capability

The static package serves the browser assets. The server package is the relevant output when the deployment needs Quasar's Common Lisp runtime behavior as well. A missing frontend asset, a runtime startup failure and a backend connection failure are different problems; packaging them explicitly helps keep those paths distinguishable.

The hosted merge records exact-main Nix, Lisp, saved-image smoke and Prolog verification. This post does not claim a fresh build or a new performance benchmark. The declared build inputs remain part of reproducing the packaged runtime; a package definition is not proof that every reader already has access to every dependency.

## Android relationship

The separately released native Quasar phone client is not this SBCL executable repackaged as an APK. Static web, hosted runtime and native phone client share product context, but they have different execution boundaries. Feature parity should be established operation by operation, not assumed from their names.

For the phone app, use the actual v0.3.0-alpha release assets in the Wear repository. The Android special covers credential validation, package verification and the system installation prompt rather than conflating those with the server build.

Build definitions: <https://github.com/lost-rob0t/quasar>
Android release: <https://github.com/lost-rob0t/starintel-wearos/releases/tag/v0.3.0-alpha>

## Sources

Standalone frontend distribution: <https://github.com/lost-rob0t/quasar/commit/b2839355a40a006b33f0b203032fe0bfc4d461d5>
Hosted runtime and configuration: <https://github.com/lost-rob0t/quasar/commit/cb55fdf24505c1edfd226db6c3cbcfbb0af1d22b>
Canonical merge and recorded verification: <https://github.com/lost-rob0t/quasar/commit/44f977cdecb91d78cd77e35cb287503c135dee50>
