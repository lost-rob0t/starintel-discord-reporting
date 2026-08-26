% StarIntel report style knowledge base.
%
% This file is intentionally data-first. The gate consumes these facts; new
% rejected reports should add examples and only promote repeated, objective
% patterns into hard rules.

% banned_phrase(Category, Phrase).
banned_phrase(fake_gravitas, "substantially verified").
banned_phrase(fake_gravitas, "recovered official record").
banned_phrase(fake_gravitas, "implied framing").
banned_phrase(lawyerly_caveat, "it is important to note").
banned_phrase(lawyerly_caveat, "there is no evidence").
banned_phrase(lawyerly_caveat, "this does not necessarily mean").
banned_phrase(release_note_slop, "significant improvements").
banned_phrase(release_note_slop, "we are thrilled to announce").
banned_phrase(release_note_slop, "groundbreaking").
banned_phrase(release_note_slop, "comprehensive solution").

% qualifier(Phrase). Two or more distinct qualifiers in one report trigger the
% bureaucratic-density rule.
qualifier("substantially").
qualifier("materially").
qualifier("not established").
qualifier("does not prove").
qualifier("cannot conclude").
qualifier("the available evidence").
qualifier("the record does not").

% preferred_uncertainty(Phrase).
preferred_uncertainty("it mostly checks out, but").
preferred_uncertainty("we could verify most of it, but").
preferred_uncertainty("the records back most of this, but").

% rejected_example(Id, Source, Category, Text).
% `Source` records why the example is trusted as a negative style example.
rejected_example(
    assistant_failure_2026_08_25_oregon,
    user_rejected,
    fake_gravitas,
    "The Wire's Oregon quintuple-homicide chain is substantially verified, but the implied body-dump framing is not established by the recovered official record."
).

% Smaller synthetic examples distilled from the same rejected style family.
rejected_example(
    seed_fake_gravitas,
    style_contract,
    fake_gravitas,
    "The claim is substantially verified by the recovered official record."
).
rejected_example(
    seed_lawyerly_caveat,
    style_contract,
    lawyerly_caveat,
    "It is important to note that this does not necessarily mean anything changed."
).
rejected_example(
    seed_bureaucratic_density,
    style_contract,
    bureaucratic_density,
    "The available evidence materially supports the claim, but the record does not establish the rest."
).

% accepted_example(Id, Source, Text).
accepted_example(
    preferred_plain_uncertainty,
    user_preferred,
    "It mostly checks out, but the approval trail is still missing."
).
accepted_example(
    preferred_direct_followup,
    style_contract,
    "It mostly checks out, but one part is still unverified. The contract ended. The access logs are still missing."
).
