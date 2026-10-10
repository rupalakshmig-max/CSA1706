from collections import deque
graph={'1':['2','3'],
       '2':['4','5'],
       '3':[],
       '4':['5'],
       '5':[]}
# DFS - Depth First Search
def dfs(start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(node, visited)

    return visited

print("DFS:", " -> ".join(dfs('1')))
