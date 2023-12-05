with open("../input/day5.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle) + [""]
seeds, map, reversedmaps, i, b = [int(i) for i in aocinput[0].split(":")[1].split()], [], [], 0, 0
for _, line in enumerate(aocinput[2:]):
    if len(line) == 0:
        newseeds = []
        reversedmaps.insert(0, map)
        for seed in seeds:
            dest = seed
            for m in [m for m in map if seed >= m[1] and seed < m[1] + m[2]]:
                dest = m[0] + (seed - m[1])
            newseeds.append(dest)
        seeds, map = newseeds, []
    elif not ":" in line:
        map.append([int(i) for i in line.split()])
print("a:", min(seeds))
seeds = [int(i) for i in aocinput[0].split(":")[1].split()]
while b == 0:
    dest = i
    for map in reversedmaps:
        for m in [m for m in map if dest >= m[0] and dest < (m[0] + m[2])]:
            dest = m[1] + (dest - m[0])
            break
    for p in range(0, len(seeds) - 1, 2):
        b = i if dest >= seeds[p] and dest < (seeds[p] + seeds[p + 1]) else b
    if i % 100000 == 0:
        print("still going strong...", i)
    i += 1
print("b:", b)
