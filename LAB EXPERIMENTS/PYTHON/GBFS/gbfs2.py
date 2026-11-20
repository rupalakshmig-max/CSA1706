import heapq

graph = {
    'P': ['R', 'C', 'A'],
    'R': ['E'],
    'C': ['R', 'M', 'U'],
    'E': ['U', 'S'],
    'A': ['M'],
    'M': ['U', 'L'],
    'U': ['N', 'S'],
    'L': ['N'],
    'N': ['S'],
    'S': []
}

h = {
    'P': 10,
    'R': 8,
    'C': 6,
    'E': 3,
    'A': 11,
    'M': 9,
    'U': 4,
    'S': 0,
    'L': 9,
    'N': 6
}

def gbfs(start, goal):
    queue = [(h[start], start, [start])]
    visited = set()

    while queue:
        heuristic, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (h[neighbor], neighbor, path + [neighbor])
                )

gbfs('P', 'S')
