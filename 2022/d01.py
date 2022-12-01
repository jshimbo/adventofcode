def topN(arr, x, top):
    arr.append(x)
    return (sorted(arr, reverse=True)[:top])


def solve(lines, top):
    calories = []
    tmp_sum = 0

    for l in lines:
        s = l.strip()
        if s:
            tmp_sum += int(s)
        else:
            calories = topN(calories, tmp_sum, top)
            tmp_sum = 0

    # repeat because last line in input isn't blank
    calories = topN(calories, tmp_sum, top)
    return sum(calories)


def main():
    input_file = "input/d01"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, 1))
    print("Answer to part 2:", solve(lines, 3))


if __name__ == '__main__':
    main()
