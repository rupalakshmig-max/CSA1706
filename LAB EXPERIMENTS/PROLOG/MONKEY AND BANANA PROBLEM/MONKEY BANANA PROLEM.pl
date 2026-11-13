initial_state(at_door, on_floor, no, no).

goal_state(state(_, _, _, has)).

move(
    state(at_door, on_floor, no, no),
    state(middle, on_box, yes, no),
    climb_box
).

move(
    state(middle, on_box, yes, no),
    state(middle, on_box, yes, has),
    grasp_banana
).

move(
    state(X, on_floor, no, no),
    state(Y, on_floor, no, no),
    walk(X, Y)
) :-
    X \= Y.

solve(State, []) :-
    goal_state(State).

solve(State, [Action | Rest]) :-
    move(State, NextState, Action),
    solve(NextState, Rest).