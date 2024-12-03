import re


def solve2(lines):
    input = []
    line = "".join(lines)
    muls = line.split("do()")
    for mul in muls:
        s = mul.split("don't()")
        input.append(s[0])
    return solve1(input)


def solve1(lines):
    total = 0
    for line in lines:
        muls = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in muls:
            nums = re.findall(r"\d+", mul)
            total += int(nums[0]) * int(nums[1])
    return total


def main():
    input_file = "input/d03.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
