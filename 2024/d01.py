def makeLists(lines):
    lists = [[], []]
    total = 0

    for l in lines:
        tmp = l.split()
        lists[0].append(int(tmp[0]))
        lists[1].append(int(tmp[1]))

    lists[0].sort()
    lists[1].sort()

    return lists


def checkLists(val0, list1, i1):
    result = 0
    list_len = len(list1)
    val1 = list1[i1]

    while val0 == val1 and i1 < list_len:
        result += val0
        i1 += 1
        val1 = list1[i1]

    return result


def solve2(lines):
    lists = makeLists(lines)
    total = 0

    i1 = 0  # right index
    list_len = len(lists[0])

    for _, val0 in enumerate(lists[0]):
        while val0 > lists[1][i1] and i1 < (list_len - 1):
            i1 += 1

        sub_total = checkLists(val0, lists[1], i1)
        total += sub_total

    return total


def solve1(lines):
    lists = makeLists(lines)
    total = 0

    for l, r in zip(lists[0], lists[1]):
        total += abs(l - r)

    return total


def main():
    input_file = "input/d01.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
