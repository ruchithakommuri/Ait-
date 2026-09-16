groups = ['A', 'B', 'C', 'D']

colors = ['Red', 'Green', 'Blue']

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]

color = {}

for group in groups:
    for c in colors:
        if all(
            not (x == group and color.get(y) == c)
            and not (y == group and color.get(x) == c)
            for x, y in edges
        ):
            color[group] = c
            break

print(color)
