fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).
fruit(mango, yellow).

show_fruit :-
    fruit(X, Y),
    write(X),
    write(' - '),
    write(Y),
    nl,
    fail.

show_fruit.