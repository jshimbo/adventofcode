def solve1(lines):
    answer = 0
    for l in lines:
        sections = l.split(",")
        inner = [int(x) for x in sections[0].split("-")]
        outer = [int(x) for x in sections[1].split("-")]

        if outer[0] == inner[0] or outer[1] == inner[1]:
            answer += 1
        else:
            if inner[0] < outer[0]:
                # swap
                tmp = outer
                outer = inner
                inner = tmp
            if outer[1] >= inner[1]:
                # fully contains
                answer += 1

    return answer


def solve2(lines):
    answer = 0
    for l in lines:
        sections = l.split(",")
        inner = [int(x) for x in sections[0].split("-")]
        outer = [int(x) for x in sections[1].split("-")]

        if outer[0] == inner[0] or outer[1] == inner[1]:
            answer += 1
        else:
            if inner[0] < outer[0]:
                # swap
                tmp = outer
                outer = inner
                inner = tmp
            if outer[1] >= inner[0]:
                # overlaps
                answer += 1

    return answer


def main():
    # filename = "input/d04-pre"
    filename = "input/d04"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve1(lines))
    print("Part 2:", solve2(lines))


if __name__ == '__main__':
    main()
