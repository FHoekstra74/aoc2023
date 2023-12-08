import math

with open("../input/day8.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
directions, map, alla = aocinput[0], {}, []
for i in aocinput[2:]:
    node = i.split("=")[0].strip()
    map[node] = i.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")
    if node.endswith("A"):
        alla.append(node)

cur, stop, a, count, firstz = "AAA", False, 0, 1, []
while not stop:
    for c in directions:
        cur = map[cur][0] if c == "L" else map[cur][1]
        a = count if cur == "ZZZ" else a
        for i, node in enumerate(alla):
            alla[i] = map[node][0] if c == "L" else map[node][1]
            if alla[i].endswith("Z"):
                firstz.append(count)
                if len(firstz) == len(alla):
                    stop = True
        count += 1
b = firstz[0]
for i in firstz[1:]:
    b = (i * b) // math.gcd(i, b)
print(a, b)
