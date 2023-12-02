with open("../input/day2.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
a, b = 0, 0
for line in aocinput:
    gameid, game = line.split(":")
    fewest, oke = {"green": 0, "red": 0, "blue": 0}, 1
    for gameset in game.split("; "):
        used = {"green": 0, "red": 0, "blue": 0}
        for cube in gameset.strip().split(", "):
            number, color = cube.split(" ")
            fewest[color] = max(fewest[color], int(number))
            used[color] += int(number)
        if used["red"] > 12 or used["green"] > 13 or used["blue"] > 14:
            oke = 0
    a = a + int(gameid.split(" ")[1]) if oke == 1 else a
    b += fewest["red"] * fewest["green"] * fewest["blue"]
print(a, b)
