with open("../input/day6.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
times = [int(i) for i in aocinput[0].split(":")[1].split()] + [
    int("".join([i for i in aocinput[0].split(":")[1].split()]))
]
records = [int(i) for i in aocinput[1].split(":")[1].split()] + [
    int("".join([i for i in aocinput[1].split(":")[1].split()]))
]
a, wins = 1, []
for race in range(5):
    t, r = times[race], records[race]
    for i in range(t + 1):
        if (t - i) * i > r:
            wins.append(t - (2 * i) + 1)
            break
for i in wins[:4]:
    a *= i
print(a, wins[-1])
