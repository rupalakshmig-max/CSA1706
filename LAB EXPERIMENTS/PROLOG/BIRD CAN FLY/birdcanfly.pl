bird(parrot).
bird(pigeon).
bird(sparrow).
bird(ostrich).
bird(penguin).

can_fly(parrot).
can_fly(pigeon).
can_fly(sparrow).

cannot_fly(ostrich).
cannot_fly(penguin).

check(X) :-
    can_fly(X),
    write(X),
    write(' can fly').

check(X) :-
    cannot_fly(X),
    write(X),
    write(' cannot fly').