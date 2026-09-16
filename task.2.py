grid = [
    ['S', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', 'X', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)

current = start
path = [current]

while current != goal:
    x, y = current
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    best = None
    best_distance = float('inf')

    for i, j in moves:
        if 0 <= i < 6 and 0 <= j < 6 and grid[i][j] != 'X':
            if (i, j) not in path:
                distance = abs(goal[0] - i) + abs(goal[1] - j)

                if distance < best_distance:
                    best_distance = distance
                    best = (i, j)

    if best is None:
        print("No path found")
        break

    current = best
    path.append(current)

else:
    print("Path:", path)
    print("Number of steps:", len(path) - 1)
