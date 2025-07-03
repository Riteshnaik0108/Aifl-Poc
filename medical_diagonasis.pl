% Symptoms for flu, cold, fungal infection
symptom(flu).
symptom(fungal_infection).
symptom(cold).

flu(X) :-
    has_symptom(X, fever),
    has_symptom(X, cough),
    has_symptom(X, fatigue),
    has_symptom(X, body_aches),
    has_symptom(X, sore_throat),
    has_symptom(X, runny_nose).

cold(X) :-
    has_symptom(X, cough),
    has_symptom(X, sore_throat),
    has_symptom(X, stuffy_nose),
    has_symptom(X, sneezing),
    has_symptom(X, mild_fever).

fungal_infection(X) :-
    has_symptom(X, redness),
    has_symptom(X, itching),
    has_symptom(X, scaling).

% Ask the user about symptoms
has_symptom(Person, Symptom) :-
    ask(Person, Symptom),
    response(Person, Symptom, yes).

ask(Person, Symptom) :-
    format('Does ~w have ~w? (yes/no): ', [Person, Symptom]),
    read(Response),
    nl,
    assert(response(Person, Symptom, Response)).

% Diagnosing
diagnose(Person) :-
    (   flu(Person) ->
        format('~w likely has the flu.~n', [Person])
    ;   fungal_infection(Person) ->
        format('~w likely has a fungal infection.~n', [Person])
    ;   cold(Person) ->
        format('~w likely has a cold.~n', [Person])
    ;   format('Unable to diagnose.~n')
    ).

% Clear stored responses (use before re-diagnosis)
clear_responses :- retractall(response(_, _, _)).
