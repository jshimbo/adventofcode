def getMove(t):
    res = ""
    if t == ("A", "Y") or t == ("B", "X") or t == ("C", "Z"):
        res = "X"  # rock
    elif t == ("A", "Z") or t == ("B", "Y") or t == ("C", "X"):
        res = "Y"  # paper
    elif t == ("A", "X") or t == ("B", "Z") or t == ("C", "Y"):
        res = "Z"  # scissors
    else:
        print("Fatal error in getMove")

    return res


def jkp(t):
    points = {"X": 1, "Y": 2, "Z": 3}
    res = 0

    if t == ("A", "X") or t == ("B", "Y") or t == ("C", "Z"):
        res = 3  # tie
    elif t == ("A", "Y") or t == ("B", "Z") or t == ("C", "X"):
        res = 6  # win
    elif t == ("A", "Z") or t == ("B", "X") or t == ("C", "Y"):
        res = 0  # lose
    else:
        print("Fatal error in jkp")

    res += points[t[1]]

    return res


def solve1(lines):
    score = 0
    for l in lines:
        score += jkp(l)
    return score


def solve2(lines):
    score = 0

    for l in lines:
        she = l[0]
        me = getMove(l)
        score += jkp((she, me))

    return score


def main():
    input_file = "input/d02"
    lines = []
    with open(input_file) as fp:
        lines = [tuple(line.split()) for line in fp]

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == '__main__':
    main()
