with open("../input/day11.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
map, points, emptyx, emptyy, a, b = {}, [], set(), set(), 0, 0
for y, line in enumerate(aocinput):
    found = False
    for x, c in enumerate(line):
        map[(x, y)] = c
        if c == "#":
            points.append((x, y))
            found = True
    if not found:
        emptyy.add(y)

for x in range(len(aocinput[0])):
    found = False
    for y in range(len(aocinput)):
        if map[(x, y)] == "#":
            found = True
    if not found:
        emptyx.add(x)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        combi = [points[i], points[j]]
        dist = abs(combi[0][0] - combi[1][0]) + abs(combi[0][1] - combi[1][1])
        a, b = a + dist, b + dist
        for x in range(
            min(combi[0][0], combi[1][0]), max(combi[0][0], combi[1][0]) + 1
        ):
            if x in emptyx:
                b += 1000000 - 1
                a += 1
        for y in range(
            min(combi[0][1], combi[1][1]), max(combi[0][1], combi[1][1]) + 1
        ):
            if y in emptyy:
                b += 1000000 - 1
                a += 1
print(a, b)
