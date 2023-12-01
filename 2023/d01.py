numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def getFirstNumber(s):
    first_index = 99999
    first_value = 0
    for k, v in numbers.items():
        i = s.find(k)
        if i != -1 and i < first_index:
            first_index = i
            first_value = v

    for i, c in enumerate(s):
        if c.isdigit() and i < first_index:
            first_value = int(c)
            break

    return first_value


def getLastNumber(s):
    last_index = -1
    last_value = 0

    for k, v in numbers.items():
        i = s.rfind(k)
        if i != -1 and i > last_index:
            last_index = i
            last_value = v

    for i, c in enumerate(s):
        if c.isdigit() and i > last_index:
            last_value = int(c)
            last_index = i

    return last_value


def solve2(lines):
    total = 0

    for l in lines:
        s = l.strip()
        first = getFirstNumber(s)
        last = getLastNumber(s)
        total += first * 10 + last
    return total


def solve1(lines):
    total = 0

    for l in lines:
        s = l.strip()
        first_digit = True
        for c in s:
            if c.isdigit():
                i = int(c)
                if first_digit:
                    first = last = i
                    first_digit = False
                else:
                    last = i

        total += first * 10 + last
    return total


def main():
    input_file = "input/d01.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
