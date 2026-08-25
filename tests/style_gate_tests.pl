:- begin_tests(style_gate).
:- consult('../scripts/style_gate.pl').

test(plain_uncertainty_passes) :-
    style_ok("It mostly checks out, but the approval trail is still missing.").

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
