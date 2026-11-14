edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).
edge(c, e, 6).
edge(d, e, 3).

heuristic(a, 5).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 0).

best_first(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

search([[Goal | Rest] | _], Goal, [Goal | Rest]).

search([ [Current | Rest] | OtherPaths], Goal, Path) :-
    findall(
        [Next, Current | Rest],
        (edge(Current, Next, _),
         \+ member(Next, [Current | Rest])),
        NewPaths
    ),
    append(OtherPaths, NewPaths, AllPaths),
    sort_paths(AllPaths, Sorted),
    search(Sorted, Goal, Path).

sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_score, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_score([Node | _], H) :-
    heuristic(Node, H).