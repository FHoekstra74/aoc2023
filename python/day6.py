with open("../input/day6.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
times = [int(i) for i in aocinput[0].split(":")[1].split()] + [int("".join([i for i in aocinput[0].split(":")[1].split()]))]
records = [int(i) for i in aocinput[1].split(":")[1].split()] + [int("".join([i for i in aocinput[1].split(":")[1].split()]))]
a, b = 0, 0
for race in range(5):
    t, r, wins = times[race], records[race], 0
    for i in range(t + 1):
        wins = wins + 1 if (t - i) * i > r else wins
    if race == 4:
        b = wins
    else:
        a = wins if a == 0 else a * wins
print(a, b)
