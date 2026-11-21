
# Map Colouring using Backtracking

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E', 'F'],
    'C': ['B', 'E', 'F'],
    'D': ['A', 'B', 'E', 'G', 'H'],
    'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
    'F': ['B', 'C', 'E', 'H', 'I'],
    'G': ['D', 'E', 'H', 'J'],
    'H': ['D', 'E', 'F', 'G', 'I', 'J'],
    'I': ['E', 'F', 'H', 'J'],
    'J': ['G', 'H', 'I']
}

colors = ['Blue', 'Green', 'Red', 'Yellow']
color_map = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if color_map.get(neighbor) == color:
            return False
    return True

def graph_coloring(nodes, index):
    if index == len(nodes):
        return True

    node = nodes[index]

    for color in colors:
        if is_safe(node, color):
            color_map[node] = color

            if graph_coloring(nodes, index + 1):
                return True

            del color_map[node]

    return False

nodes = list(graph.keys())

if graph_coloring(nodes, 0):
    print("Map Coloring Solution:")
    for node in nodes:
        print(node, ":", color_map[node])
else:
    print("No solution exists")
