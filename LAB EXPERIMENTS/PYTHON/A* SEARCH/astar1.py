graph = {
    'S': {'A': 3, 'D': 4},
    'A': {'S': 3, 'B': 4, 'D': 5},
    'B': {'A': 4, 'C': 4, 'E': 5},
    'C': {'B': 4},
    'D': {'S': 4, 'A': 5, 'E': 2},
    'E': {'D': 2, 'B': 5, 'F': 4},
    'F': {'E': 4, 'G': 3.5},
    'G': {'F': 3.5}
}

h = {
    'S': 11.5,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

def a_star(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

a_star('S', 'G')
