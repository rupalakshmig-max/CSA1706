from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
# DFS - Depth First Search
def dfs(start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(node, visited)

    return visited

print("DFS:", " -> ".join(dfs('A')))
