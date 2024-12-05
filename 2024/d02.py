def isSafeBasic(readings):
    direction = 0
    previous = 0
    result = True

    for i, r in enumerate(readings):
        if i > 0:
            diff = previous - r
            if diff == 0:
                result = False
                break
            elif diff < 0:  # increasing
                if direction < 0:
                    result = False
                    break
                else:
                    direction = 1
            else:  # decreasing
                if direction > 0:
                    result = False
                    break
                else:
                    direction = -1

            # Direction has been checked, now check magnitude
            if abs(diff) > 3:
                result = False
                break

        previous = r

    return result


def solve(lines):
    total = 0
    for line in lines:
        readings = [int(s) for s in line.split()]
        if isSafeBasic(readings):
            total += 1
    return total


def main():
    input_file = "input/d02.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines))


if __name__ == "__main__":
    main()
