with open("../input/day3.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)

map, a, partnumbers, gears = {}, 0, [], {}
maxx, maxy = len(aocinput[0]), len(aocinput)

for y, line in enumerate(aocinput):
    part = ""
    for x, c in enumerate(line):
        map[(x, y)] = c
        if c == "*":
            gears[(x, y)] = []
        if c.isnumeric():
            part = part + c
        else:
            if part != "":
                partnumbers.append((x - len(part), y, part))
            part = ""
    if part != "":
        partnumbers.append((maxx - len(part), y, part))

for item in partnumbers:
    partnumber, xpart, ypart, symbolsfound = item[2], item[0], item[1], 0
    for x in range(len(partnumber) + 2):
        cx = xpart + x - 1
        for y in range(3):
            cy = ypart + y - 1
            if cx > -1 and cx < maxx and cy > -1 and cy < maxy:
                c = map[cx, cy]
                if c == "*":
                    gears[(cx, cy)].append((partnumber))
                if not c.isnumeric() and c != ".":
                    symbolsfound += 1
    if symbolsfound > 0:
        a += int(partnumber)
print(a, sum([int(v[0]) * int(v[1]) for k, v in gears.items() if len(v) > 1]))
