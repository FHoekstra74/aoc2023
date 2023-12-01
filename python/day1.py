with open("../input/day1.txt", "r", encoding="utf-8") as filehandle:
    aocinput = list(line.rstrip() for line in filehandle)
a, b = 0, 0
for _, line in enumerate(aocinput):
    digitsa, digitsb = [], []
    for pos, val in enumerate(line):
        if val.isnumeric():
            digitsa.append(val)
            digitsb.append(val)
        else:
            for c, word in enumerate(
                [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ]
            ):
                if line[pos : pos + len(word)] == word:
                    digitsb.append(str(c + 1))
    a += int(digitsa[0] + digitsa[-1])
    b += int(digitsb[0] + digitsb[-1])
print(a, b)
