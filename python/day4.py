with open("../input/day4.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
bcards, a = [1 for line in aocinput], 0
for card, line in enumerate(aocinput):
    winningcards, cards = (t.strip().split() for t in line.split(":")[1].split("|"))
    wins = 0
    for s in cards:
        wins = wins + 1 if s in winningcards else wins
    if wins > 0:
        a += pow(2, wins - 1)
    for k in range(wins):
        bcards[card + k + 1] += bcards[card]
print(a, sum(bcards))
