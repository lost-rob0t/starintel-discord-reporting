#!/usr/bin/env swipl
:- initialization(main, main).
:- use_module(library(readutil)).
:- use_module(library(lists)).

% Keep the hard gate narrow and explainable. STYLE.md remains the human contract;
% this expert system catches recurring, objective tone failures before publish.

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

preferred_uncertainty("it mostly checks out, but").
preferred_uncertainty("we could verify most of it, but").
preferred_uncertainty("the records back most of this, but").

violation(Text, no_em_dash, "use a comma, colon, semicolon, or new sentence instead") :-
    sub_string(Text, _, _, _, "—").

violation(Text, Rule, Detail) :-
    string_lower(Text, Lower),
    banned_phrase(Rule, Phrase),
    sub_string(Lower, _, _, _, Phrase),
    format(string(Detail), "banned phrase: ~q", [Phrase]).

% Dense chains of institutional qualifiers are a reliable slop smell even when
% no single banned phrase fires. Two or more in one report is a hard failure.
qualifier("substantially").
qualifier("materially").
qualifier("not established").
qualifier("does not prove").
qualifier("cannot conclude").
qualifier("the available evidence").
qualifier("the record does not").

qualifier_hit(Text, Phrase) :-
    string_lower(Text, Lower),
    qualifier(Phrase),
    sub_string(Lower, _, _, _, Phrase).

violation(Text, bureaucratic_density, Detail) :-
    findall(P, qualifier_hit(Text, P), Hits0),
    sort(Hits0, Hits),
    length(Hits, Count),
    Count >= 2,
    atomic_list_concat(Hits, ', ', Joined),
    format(string(Detail), "too many analyst/compliance qualifiers (~d): ~w; say the uncertainty plainly", [Count, Joined]).

lint_text(Text, Violations) :-
    findall(Rule-Detail, violation(Text, Rule, Detail), Raw),
    sort(Raw, Violations).

style_ok(Text) :-
    lint_text(Text, []).

lint_file(Path, Violations) :-
    read_file_to_string(Path, Text, []),
    lint_text(Text, Violations).

print_violation(Path, Rule-Detail) :-
    format(user_error, "STYLE FAIL ~w [~w]: ~w~n", [Path, Rule, Detail]).

check_file(Path, Failed0, Failed) :-
    (   exists_file(Path)
    ->  lint_file(Path, Violations),
        (   Violations == []
        ->  format("STYLE OK   ~w~n", [Path]),
            Failed = Failed0
        ;   maplist(print_violation(Path), Violations),
            Failed = true
        )
    ;   format(user_error, "STYLE FAIL ~w [missing_file]: file does not exist~n", [Path]),
        Failed = true
    ).

check_files(Paths) :-
    foldl(check_file, Paths, false, Failed),
    ( Failed == true -> halt(1) ; halt(0) ).

print_help :-
    writeln("usage: swipl -q -s scripts/style_gate.pl -- REPORT.md [REPORT.md ...]"),
    writeln("Fails when a report violates objective tone rules from STYLE.md."),
    writeln("Preferred plain uncertainty examples:"),
    forall(preferred_uncertainty(P), format("  - ~s~n", [P])).

main(Argv) :-
    (   Argv == []
    ->  print_help,
        halt(2)
    ;   check_files(Argv)
    ).
