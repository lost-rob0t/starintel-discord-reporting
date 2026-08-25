#!/usr/bin/env swipl
:- use_module(library(readutil)).
:- use_module(library(lists)).
:- discontiguous violation/3.

:- prolog_load_context(directory, ScriptDir),
   directory_file_path(ScriptDir, '../kb/style_kb.pl', StyleKb),
   consult(StyleKb).

% Keep the hard gate narrow and explainable. STYLE.md remains the human contract;
% kb/style_kb.pl holds learned examples and objective recurring patterns.

violation(Text, no_em_dash, "use a comma, colon, semicolon, or new sentence instead") :-
    sub_string(Text, _, _, _, "—").

violation(Text, Rule, Detail) :-
    string_lower(Text, Lower),
    banned_phrase(Rule, Phrase),
    sub_string(Lower, _, _, _, Phrase),
    format(string(Detail), "banned phrase: ~q", [Phrase]).

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

rejected_example_still_rejected(Id) :-
    rejected_example(Id, _, _, Text),
    lint_text(Text, Violations),
    Violations \== [].

accepted_example_still_accepted(Id) :-
    accepted_example(Id, _, Text),
    style_ok(Text).

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
    writeln("usage: swipl -q -s scripts/style_gate.pl -g run_cli -- REPORT.md [REPORT.md ...]"),
    writeln("Fails when a report violates objective tone rules from STYLE.md / kb/style_kb.pl."),
    writeln("Preferred plain uncertainty examples:"),
    forall(preferred_uncertainty(P), format("  - ~s~n", [P])).

main(Argv) :-
    (   Argv == []
    ->  print_help,
        halt(2)
    ;   check_files(Argv)
    ).

run_cli :-
    current_prolog_flag(argv, Argv),
    main(Argv).
