def getchar(line):
    global ptr
    if ptr < len(line):
        res = line[ptr]
    else:
        res = 0
    ptr += 1
    return res


def score_comps(completions):
    score_table = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for comps in completions:
        score = 0
        for c in comps:
            score *= 5
            score += score_table[c]
        scores.append(score)
    midpoint = int(len(scores)/2)
    final_score = sorted(scores)[midpoint]
    return final_score


def get_match2(line, c):
    global ptr
    global stack
    matches = {'{': '}', '[': ']', '<': '>', '(': ')'}
    openers = matches.keys()

    if c not in openers:
        print("Error: Expected opener, got", c, "in pos", ptr)
        return c

    x = getchar(line)
    while x:
        if x in openers:
            stack.append(c)
            res = get_match2(line, x)
            if res:
                return res

        else:
            if x == matches[c]:
                # print("Matched", c, x)
                if len(stack):
                    c = stack.pop()
                else:
                    return False
            else:
                # it's a non-matching closer
                # print("Expected", matches[c], "got", x, "in pos", ptr)
                return x  # no match

        x = getchar(line)

    # fall through final
    stack.append(c)
    res = []
    for n in stack:
        res.append(matches[n])
    res.reverse()
    return res


def part2(lines):

    scoreboard = {')': 3, ']': 57, '}': 1197, '>': 25137, 'E': 0}
    score = 0
    global ptr
    global stack
    completions = []

    for line in lines:
        # print("-----")
        ptr = 0
        stack = []
        c = getchar(line)
        res = get_match2(line, c)
        if type(res) is list:
            completions.append(''.join(res))
        else:
            score += scoreboard[res]
    score2 = score_comps(completions)
    return score, score2


ptr = 0
stack = []


def main():
    answer1 = 0
    answer2 = 0

    input_file = 'input/10-input'

    lines = []
    with open(input_file) as fp:
        for line in fp:
            lines.append(line.strip())

    answer1, answer2 = part2(lines)

    print("Answers:")
    print("  Part 1", answer1)
    print("  Part 2", answer2)


if __name__ == '__main__':
    main()
