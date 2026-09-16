cost = [
    [0, 2, 4, 0],
    [2, 0, 3, 0],
    [4, 3, 0, 2],
    [0, 0, 2, 0]
]

totalCost = cost[0][1] + cost[1][2] + cost[2][3]

print("Robot Path: A -> B -> C -> G")
print("Total Cost:", totalCost)