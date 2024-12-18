from functools import cmp_to_key

rules = {}


def cmpPages(left, right):
    global rules
    result = 0
    if left in rules and right in rules[left]:
        result = -1
    elif right in rules and left in rules[right]:
        result = 1

    return result


def checkSeq(seq, rules):
    for i, x in enumerate(seq):
        while i > 0:
            i -= 1
            if x in rules and seq[i] in rules[x]:
                return False
    return True


def solve(lines, part):
    total = 0
    get_rules = True
    global rules

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
                get_rules = not get_rules
        else:
            seq = list(x.strip() for x in line.split(","))
            if part == 1:
                if checkSeq(seq, rules):
                    midpoint = len(seq) // 2
                    total += int(seq[midpoint])
            else:
                if not checkSeq(seq, rules):
                    seq2 = sorted(seq, key=cmp_to_key(cmpPages))
                    midpoint = len(seq2) // 2
                    total += int(seq2[midpoint])

    return total


def main():
    input_file = "input/d05.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, 1))
    print("Answer to part 2:", solve(lines, 2))


if __name__ == "__main__":
    main()
