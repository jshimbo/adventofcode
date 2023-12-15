def hash(step):
    curval = 0
    for c in step:
        curval += ord(c)
        curval *= 17
        curval = curval % 256
    return curval


def getFocusingPower(boxes):
    result = 0
    for box_num, row in enumerate(boxes):
        for slot, item in enumerate(row):
            s = item.split(" ")
            result += (box_num + 1) * (slot + 1) * int(s[1])

    return result


def solve2(lines):
    boxes = list([] for _ in range(256))

    for step in lines[0].strip().split(","):
        if step[-1] == "-":
            s = step[:-1]
            i = hash(s)
            for x, item in enumerate(boxes[i]):
                if s in item:
                    boxes[i].pop(x)
        else:  # equal sign
            s = step.split("=")
            i = hash(s[0])
            updated = False
            for x, item in enumerate(boxes[i]):
                if s[0] == item.split(" ")[0]:
                    boxes[i][x] = " ".join(s)
                    updated = True
                    break
            if not updated:
                boxes[i].append(" ".join(s))

    return getFocusingPower(boxes)


def solve1(lines):
    result = 0

    for step in lines[0].strip().split(","):
        curval = hash(step)
        result += curval

    return result


def main():
    input_file = "input/d15.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 1:", solve2(lines))


if __name__ == "__main__":
    main()
