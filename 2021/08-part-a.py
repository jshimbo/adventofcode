
def get_output_values(s):
    return(s.split('|')[1].strip())


def solve1(lines):
    bins = {}
    for line in lines:
        digits = line.strip().split()
        for digit in digits:
            l = len(digit)
            bins[l] = bins.get(l, 0) + 1
    # print(bins)
    # 1, 4, 7, and 8
    return(bins[2] + bins[4] + bins[3] + bins[7])


def solve2(lines):
    bins = {}
    for line in lines:
        digits = line.strip().split()
        for digit in digits:
            # l = len(digit)
            bins[digit] = bins.get(digit, 0) + 1
    # print(bins)
    return


def main():
    input_file = "08-input"

    lines = list(map(get_output_values, open(input_file).readlines()))

    bins = {}
    for line in lines:
        digits = line.strip().split()
        for digit in digits:
            l = len(digit)
            bins[l] = bins.get(l, 0) + 1

    answer1 = solve1(lines)
    print("Answer 1", answer1)
    answer2 = solve2(lines)
    print("Answer 2", answer2)

    # locations = crabs.keys()
    # print(len(lines), "crabs in", len(locations), "locations")
    # print("Lowest position", min(locations))
    # print("Highest position", max(locations))

    # print("part 1 answer:", solve(crabs, lambda x: abs(x)))
    # print("part 2 answer:", solve(crabs, lambda x: abs(x)*(abs(x)+1)/2))
    return


if __name__ == '__main__':
    main()
