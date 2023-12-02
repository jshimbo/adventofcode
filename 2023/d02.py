def getPower(cubes):
    result = 1

    vals = list(cubes.values())
    for i in vals:
        result *= i

    return result


def solve2(lines):
    total = 0
    cubes = {}
    minimums = {}

    for l in lines:
        s = l.strip().split(":")
        moves = s[1].split(";")

        minimums.clear()

        for move in moves:
            cubes.clear()
            cubes["red"] = cubes["green"] = cubes["blue"] = 0

            dice = move.split(",")
            for die in dice:
                d = die.strip().split(" ")
                x = int(d[0])
                color = d[1].strip()
                cubes[color] += x

            for k, v in cubes.items():
                if v > 0 and (k not in minimums or v > minimums[k]):
                    minimums[k] = v

        total += getPower(minimums)

    return total


def impossible(cubes):
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for k, v in max_cubes.items():
        if cubes[k] > v:
            return True

    return False


def solve1(lines):
    total = 0

    for l in lines:
        s = l.strip().split(":")
        g = s[0].split(" ")
        game_number = int(g[1])
        moves = s[1].split(";")

        over_limit = False
        cubes = {}

        for move in moves:
            cubes.clear()
            cubes["red"] = cubes["green"] = cubes["blue"] = 0
            dice = move.split(",")
            for die in dice:
                d = die.strip().split(" ")
                x = int(d[0])
                color = d[1].strip()
                cubes[color] += x

            if impossible(cubes):
                over_limit = True
                break

        if not over_limit:
            total += game_number

    return total


def main():
    input_file = "input/d02.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
