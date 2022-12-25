# Day 25: Full of Hot Air

def solve(lines):
    decimal_sum = 0
    for line in lines:
        number = reversed(line)
        place = 0
        accumulator = 0
        for c in number:
            if c == '-':
                digit = -1
            elif c == "=":
                digit = -2
            else:
                digit = int(c)

            number = (5 ** place) * digit
            accumulator += number
            place += 1

        decimal_sum += accumulator

    # snafu to decimal
    accumulator = decimal_sum
    snafu_number = []

    # Start with most significant digit
    power = 0
    while accumulator > (5 ** power):
        power += 1
    power -= 1

    print("power =", power)

    while power >= 0:
        chunk = (5 ** power)
        digit = 0

        if accumulator == 0:
            snafu_number.append("0")
        elif accumulator > 0:
            while accumulator > (chunk / 2):
                accumulator -= chunk
                digit += 1
            snafu_number.append(str(digit))
        else:
            while accumulator < (chunk / -2):
                accumulator += chunk
                digit -= 1
            if digit == -1:
                snafu_number.append("-")
            elif digit == -2:
                snafu_number.append("=")
            else:
                print(f"Warning: power={power} digit={digit}")

        power -= 1

    return "".join(snafu_number)


def main():
    filename = "input/d25.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines))


if __name__ == '__main__':
    main()
