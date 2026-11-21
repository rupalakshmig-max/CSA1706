
% Forward Chaining Program

% Rule R1
% If fever and cough are true,
% then the person has common cold.

rule([fever, cough], common_cold).

% Start Forward Chaining
forward_chain(Facts, Result) :-
    sort(Facts, UniqueFacts),
    apply_rules(UniqueFacts, Result).

% Apply rules repeatedly
apply_rules(Facts, Result) :-

    findall(NewFact,
        ( rule(Conditions, NewFact),
          subset(Conditions, Facts),
          \+ member(NewFact, Facts)
        ),
        NewFacts),

    sort(NewFacts, UniqueNewFacts),

    ( UniqueNewFacts = [] ->
        Result = Facts
    ;
        append(Facts, UniqueNewFacts, UpdatedFacts),
        sort(UpdatedFacts, SortedFacts),
        apply_rules(SortedFacts, Result)
    ).

% Check whether all conditions are satisfied
subset([], _).

subset([H|T], Facts) :-
    member(H, Facts),
    subset(T, Facts).