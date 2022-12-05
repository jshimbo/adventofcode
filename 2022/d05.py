import re


def printShip(ship):
    print("~~")
    for stack in ship:
        print(stack)
    print("~~")


def getAnswer(ship):
    top_crates = []
    for deck in ship:
        top_crates.append(deck[-1:])

    answer = "".join(top_crates)
    return answer


def moveCrates(ship, cnt, src, dest, crane_model):
    # pick crates
    stack = ship[src-1]
    cache = stack[-cnt:]
    ship[src-1] = stack[:-cnt]

    if crane_model == 9000:
        cache = cache[::-1]  # reverse order of crates

    # place crates
    ship[dest-1] += cache

    return ship


def solve(crates_s, moves_s, crane_model):

    lines = crates_s.splitlines()
    lines.pop()
    num_stacks = int((len(lines[0]) + 1) / 4)

    # create empty ship
    ship = []
    for _ in range(num_stacks):
        ship.append("")

    # rotate array and use strings instead
    for layer in reversed(lines):
        width = len(layer)
        j = 0
        for x in range(1, width, 4):
            c = layer[x]
            if c != ' ':
                ship[j] += c
            j += 1

    # done initializing

    # start processing moves
    moves = moves_s.splitlines()
    for move in moves:
        x = re.findall(r'\d+', move)
        cnt = int(x[0])
        src = int(x[1])
        dest = int(x[2])
        ship = moveCrates(ship, cnt, src, dest, crane_model)

    # printShip(ship)
    return getAnswer(ship)


def main():
    filename = "input/d05"
    with open(filename) as f:
        data_parts = f.read().split("\n\n")

    print("Part 1:", solve(data_parts[0], data_parts[1], 9000))
    print("Part 1:", solve(data_parts[0], data_parts[1], 9001))


if __name__ == '__main__':
    main()
