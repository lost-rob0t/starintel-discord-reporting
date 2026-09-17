# Zara Android: Samsung Health is now a Prolog-backed data source

## Changes

- Zara Android can now read Samsung Health fitness and wellness data through the local Prolog layer. The landed surface covers SDK status, granted permissions, today's steps, sleep duration, heart-rate minimum/maximum, and exercise duration/calories.

- The integration is read-only and permission-gated. Zara resolves intent in Prolog first, then executes the physical Samsung Health read through one serialized actor. Missing permission stops the read before the vendor gateway is called.

- Samsung's Health Data SDK remains optional instead of becoming a hard dependency. Ordinary builds still work without the vendor AAR and report the SDK as unavailable. A follow-up master fix also restored the Android AutomationActivity Compose build after the integration landed.

Samsung Health integration: <https://github.com/lost-rob0t/zara/commit/6cbc73c6f894231e1216df9a5f63e51bfa75cd80>

Android build repair: <https://github.com/lost-rob0t/zara/commit/df01a886cf3e4f800458c2269a04af84a86c496c>
