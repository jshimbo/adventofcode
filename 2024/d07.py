def calc2(target, subtotal, ops, i):
    if i >= len(ops) or subtotal > target:
        return subtotal
    elif i == (len(ops) - 1):
        if subtotal * ops[i] == target:
            return target
        else:
            if subtotal + ops[i] == target:
                return target
            else:
                return int(str(subtotal) + str(ops[i]))
    else:
        x = subtotal * ops[i]
        if calc2(target, x, ops, i + 1) == target:
            return target
        else:
            x = subtotal + ops[i]
            if calc2(target, x, ops, i + 1) == target:
                return target
            else:
                x = int(str(subtotal) + str(ops[i]))
                return calc2(target, x, ops, i + 1)


def calc1(target, subtotal, ops, i):
    if i >= len(ops) or subtotal > target:
        return subtotal
    elif i == (len(ops) - 1):
        x = subtotal * ops[i]
        if x == target:
            return x
        else:
            return subtotal + ops[i]
    else:
        x = subtotal * ops[i]
        if calc1(target, x, ops, i + 1) == target:
            return target
        else:
            x = subtotal + ops[i]
            return calc1(target, x, ops, i + 1)


def solve(lines, part):
    total = 0

    for line in lines:
        tmp = line.split(":")
        target = int(tmp[0].strip())
        ops = [int(x.strip()) for x in tmp[1].split()]

        i = 0
        subtotal = ops[i]
        if part == 1:
            if calc1(target, subtotal, ops, i + 1) == target:
                total += target
        else:
            if calc2(target, subtotal, ops, i + 1) == target:
                total += target

    return total


def main():
    input_file = "input/d07.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    print("Answer to part 2:", solve(lines, part=2))


if __name__ == "__main__":
    main()
