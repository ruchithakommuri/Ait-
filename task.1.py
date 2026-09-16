from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs_two_levels(graph, start):
    visited = {start}
    queue = deque([(start, 0)])
    result = []

    while queue:
        node, level = queue.popleft()
        result.append(node)

        if level < 2:
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, level + 1))

    return result

print(bfs_two_levels(graph, 'A'))
