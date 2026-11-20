def minimax(node, depth, is_max):
    if depth == 3:
        return node

    if is_max:
        best = float('-inf')
        for child in node:
            value = minimax(child, depth + 1, False)
            best = max(best, value)
        return best

    else:
        best = float('inf')
        for child in node:
            value = minimax(child, depth + 1, True)
            best = min(best, value)
        return best


tree = [
    [
        [2, 3],
        [5, 9]
    ],
    [
        [0, 1],
        [7, 5]
    ]
]

result = minimax(tree, 0, True)
print("Minimax Value:", result)
