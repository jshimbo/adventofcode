def checkSeq(seq, rules):
    for i, x in enumerate(seq):
        while i > 0:
            i -= 1
            if x in rules and seq[i] in rules[x]:
                return False
    return True


def solve1(lines):
    total = 0
    rules = {}
    get_rules = True

    for line in lines:
        if get_rules:
            pair = [x.strip() for x in line.split("|")]
            if len(pair) > 1:
                x = pair[0]
                y = pair[1]
                if x not in rules:
                    rules[x] = [y]
                elif y not in rules[x]:
                    rules[x].append(y)
            else:
                get_rules = False
        else:
            seq = list(x.strip() for x in line.split(","))
            if checkSeq(seq, rules):
                midpoint = len(seq) // 2
                total += int(seq[midpoint])

    return total


def main():
    input_file = "input/d05.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    # print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
