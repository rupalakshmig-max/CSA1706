from collections import deque

def water_jug():
    capacity1 = 5
    capacity2 = 3
    target = 4

    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            print("Steps to get 4 litres:")
            for step in path:
                print("5L jug:", step[0], " | 3L jug:", step[1])
            return

        states = [
            (capacity1, b),  # Fill 5L jug
            (a, capacity2),  # Fill 3L jug
            (0, b),          # Empty 5L jug
            (a, 0),           # Empty 3L jug
            (a - min(a, capacity2 - b), b + min(a, capacity2 - b)),
            (a + min(b, capacity1 - a), b - min(b, capacity1 - a))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

water_jug()
