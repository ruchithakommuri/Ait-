import random

d = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4
pheromone = [[1 for j in range(n)] for i in range(n)]

best_route = None
best_distance = float('inf')

for _ in range(100):
    route = [0]
    unvisited = list(range(1, n))

    while unvisited:
        current = route[-1]
        next_city = min(unvisited, key=lambda x: d[current][x])
        route.append(next_city)
        unvisited.remove(next_city)

    route.append(0)

    distance = sum(
        d[route[i]][route[i + 1]]
        for i in range(n)
    )

    if distance < best_distance:
        best_distance = distance
        best_route = route

print("Best Route:", " -> ".join(map(str, best_route)))
print("Minimum Distance:", best_distance)
