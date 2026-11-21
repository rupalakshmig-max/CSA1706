
% Backward Chaining Program

% Known facts
fever(patient1).
headache(patient1).
joint_pain(patient1).
skin_rash(patient1).

% Rule R1
% Dengue fever can be concluded
% if fever and headache are present.

dengue_fever(X) :-
    fever(X),
    headache(X).

% Rule R2
% Another rule to prove dengue fever

dengue_fever(X) :-
    fever(X),
    joint_pain(X),
    skin_rash(X).

% Main query
% Check whether patient1 has dengue fever.
