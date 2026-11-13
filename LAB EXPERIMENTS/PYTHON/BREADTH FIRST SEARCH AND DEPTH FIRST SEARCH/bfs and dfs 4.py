from collections import deque

graph = {
    0: [1],
    1: [2, 3],
    2: [],
    3: [2, 4],
    4: [5, 6],
    5: [7],
    6: [7],
    7: []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    print("BFS:", end=" ")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(start):
    visited = set()

    def explore(node):
        if node in visited:
            return

        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            explore(neighbor)

    print("\nDFS:", end=" ")
    explore(start)

bfs(0)
dfs(0)
