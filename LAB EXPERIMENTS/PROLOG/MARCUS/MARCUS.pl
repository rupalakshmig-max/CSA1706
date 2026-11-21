
% Marcus Problem using Predicate Logic

% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tries_to_assassinate(marcus, caesar).

% Rule 1: All Pompeians are Romans
roman(X) :-
    pompeian(X).

% Rule 2: All men are people
person(X) :-
    man(X).

% Rule 3: All Romans are either loyal to Caesar
% or hate Caesar
roman(X) :-
    loyal_to(X, caesar);
    hates(X, caesar).

% Rule 4: People who try to assassinate
% a ruler are not loyal to that ruler
not_loyal_to(X, Y) :-
    tries_to_assassinate(X, Y),
    ruler(Y).

% Rule 5: A Roman who is not loyal to Caesar
% hates Caesar
hates(X, caesar) :-
    roman(X),
    not_loyal_to(X, caesar).
