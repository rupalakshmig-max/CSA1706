import heapq

graph = {
    'A': ['D', 'C', 'B'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['A', 'F'],
    'E': ['B', 'C', 'H'],
    'F': ['D', 'C', 'G'],
    'H': ['E', 'G'],
    'G': ['F', 'H']
}

h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

def greedy_best_first_search(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        heuristic, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (h[neighbor], neighbor, path + [neighbor])
                )

greedy_best_first_search('A', 'G')
