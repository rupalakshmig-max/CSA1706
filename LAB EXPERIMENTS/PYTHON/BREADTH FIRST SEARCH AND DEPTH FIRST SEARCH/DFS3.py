
# Depth First Search (DFS)

graph = {
    1: [2, 3],
    2: [5, 6],
    3: [7, 4],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7, 4]
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited


start = 1
print("DFS Traversal:", dfs(graph, start))
