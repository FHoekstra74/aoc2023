with open("../input/day16.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)

map, starts, maxx, maxy, b = {}, [], len(aocinput[0]) - 1, len(aocinput) - 1, 0
for y, line in enumerate(aocinput):
    for x, c in enumerate(line):
        map[(x, y)] = c

for x in range(maxx):
    starts.append((x, 0, "D"))
    starts.append((x, maxy, "U"))
for y in range(maxy):
    starts.append((0, y, "R"))
    starts.append((maxx, y, "L"))

for start in starts:
    beams, visited = [start], set()
    while len(beams) > 0:
        for i, (x, y, dir) in enumerate(beams):
            if not (x, y, dir) in visited:
                visited.add((x, y, dir))
                newx = x + 1 if dir == "R" else x - 1 if dir == "L" else x
                newy = y + 1 if dir == "D" else y - 1 if dir == "U" else y
                if (newx, newy) in map.keys():
                    item = map[(newx, newy)]
                    if item == "\\":
                        dir = {"R": "D", "L": "U", "U": "L", "D": "R"}[dir]
                    elif item == "/":
                        dir = {"R": "U", "L": "D", "U": "R", "D": "L"}[dir]
                    elif item == "|" and dir in ("R", "L"):
                        dir = "U"
                        beams.append((newx, newy, "D"))
                    elif item == "-" and dir in ["D", "U"]:
                        dir = "L"
                        beams.append((newx, newy, "R"))
                    beams[i] = (newx, newy, dir)
            else:
                beams.remove((x, y, dir))
    if start == (0, 0, "D"):
        print("a:", len(set((x, y) for (x, y, _) in visited)))
    b = max(b, len(set((x, y) for (x, y, _) in visited)))
print("b:", b)
