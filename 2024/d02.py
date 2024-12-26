import sys


def isSafe(readings):
    deltas = [readings[i + 1] - readings[i] for i in range(len(readings) - 1)]

    # if positive slope
    positive_slope = None

    first = deltas[0]
    if first == 0:
        return False
    else:
        positive_slope = first > 0

    for d in deltas:
        if abs(d) > 3 or (positive_slope and d <= 0) or (not positive_slope and d >= 0):
            return False

    return True


def solve(lines):

    count = 0
    for line in lines:
        readings = [int(s) for s in line.strip().split()]
        if isSafe(readings):
            count += 1

    print("Answer for part 1:", count)

    # Part 2 Naive Brute Force
    count = 0
    for line in lines:
        readings = [int(s) for s in line.strip().split()]
        if isSafe(readings):
            count += 1
            continue

        for i in range(len(readings)):
            r2 = readings.copy()
            del r2[i]
            if isSafe(r2):
                count += 1
                break

    print("Answer for part 2:", count)


def main():
    input_file = "input/d02.txt"

    with open(input_file) as f:
        lines = f.readlines()

    solve(lines)


if __name__ == "__main__":
    main()
