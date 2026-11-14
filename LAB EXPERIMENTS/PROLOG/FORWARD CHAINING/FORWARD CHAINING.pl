:- dynamic known/1.

known(a).
known(b).

rule(c) :-
    known(a),
    known(b).

rule(d) :-
    known(c).

forward :-
    rule(X),
    \+ known(X),
    !,
    assertz(known(X)),
    forward.

forward.