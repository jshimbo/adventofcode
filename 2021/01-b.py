"""
Rewrote original solution to use Python list windows
  instead of indicies
"""


def solve(lines, window_size):
    prev_sum = 0
    increased = 0

    for i in range(len(lines) - window_size + 1):
        window = lines[i: i + window_size]
        new_sum = sum(window)

        if prev_sum and (new_sum > prev_sum):
            increased += 1

        prev_sum = new_sum

    return increased


def main():
    input_file = "01-input"
    lines = list(map(int, open(input_file).readlines()))

    print("Answer to part 1:", solve(lines, 1))
    print("Answer to part 2:", solve(lines, 3))


if __name__ == '__main__':
    main()
