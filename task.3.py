import heapq

graph = {
    "Hospital": [("Junction A", 4), ("Junction B", 8)],
    "Junction A": [("Residential Area", 5)],
    "Junction B": [("Traffic Signal", 2)],
    "Traffic Signal": [("Residential Area", 3)],
    "Residential Area": [("Emergency Location", 2)],
    "Emergency Location": []
}

heuristic = {
    "Hospital": 8,
    "Junction A": 6,
    "Junction B": 5,
    "Traffic Signal": 3,
    "Residential Area": 2,
    "Emergency Location": 0
}

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    while open_list:
        f, cost, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, cost

        for neighbour, distance in graph[node]:
            new_cost = cost + distance
            new_f = new_cost + heuristic[neighbour]

            heapq.heappush(
                open_list,
                (new_f, new_cost, neighbour, path + [neighbour])
            )

path, cost = a_star("Hospital", "Emergency Location")

print("Shortest Path:", " -> ".join(path))
print("Total Path:", cost)
