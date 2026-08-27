:- begin_tests(style_gate).

:- prolog_load_context(directory, TestDir),
   directory_file_path(TestDir, '../scripts/style_gate.pl', StyleGate),
   consult(StyleGate).

test(plain_uncertainty_passes) :-
    style_ok("It mostly checks out, but the approval trail is still missing.").

test(last_assistant_failure_is_seeded) :-
    rejected_example(
        assistant_failure_2026_08_25_oregon,
        user_rejected,
        fake_gravitas,
        _
    ).

test(all_rejected_examples_stay_rejected) :-
    forall(rejected_example(Id, _, _, _), rejected_example_still_rejected(Id)).

test(all_accepted_examples_stay_accepted) :-
    forall(accepted_example(Id, _, _), accepted_example_still_accepted(Id)).

test(fake_gravitas_fails, true(member(fake_gravitas-_, Violations))) :-
    lint_text("The claim is substantially verified by the recovered official record.", Violations).

test(lawyerly_caveat_fails, true(member(lawyerly_caveat-_, Violations))) :-
    lint_text("It is important to note that this does not necessarily mean anything changed.", Violations).

test(em_dash_fails, true(member(no_em_dash-_, Violations))) :-
    lint_text("The records match — mostly.", Violations).

test(bureaucratic_density_fails, true(member(bureaucratic_density-_, Violations))) :-
    lint_text("The available evidence materially supports the claim, but the record does not establish the rest.", Violations).

test(short_direct_report_passes) :-
    style_ok("It mostly checks out, but one part is still unverified. The contract ended. The access logs are still missing.").

:- end_tests(style_gate).
