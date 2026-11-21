
% Facts
food(apple).
food(vegetable).

eats(anil, peanuts).
alive(anil).

% John likes all kinds of food
likes(john, X) :-
    food(X).

% Anything eaten by someone and not killed is food
food(X) :-
    eats(Person, X),
    alive(Person).

% Harry eats everything that Anil eats
eats(harry, X) :-
    eats(anil, X).

% John likes peanuts
likes(john, peanuts).
