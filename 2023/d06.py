def numWins(time, distance):
    wins = 0

    trial = 1
    while trial < time:
        v = trial  # velocity
        t = time - trial  # time
        d = v * t  # distance

        if d > distance:
            wins += 1

        trial += 1

    return wins


def solve2(lines):
    # parse Time
    time = "".join(lines[0].split(":")[1].strip().split())
    distance = "".join(lines[1].split(":")[1].strip().split())

    time = int(time)
    distance = int(distance)

    total = numWins(time, distance)

    return total


def solve1(lines):
    total = 1

    # parse Time
    times = lines[0].split(":")[1].strip().split()
    distances = lines[1].split(":")[1].strip().split()

    i = 0
    num_races = len(times)

    while i < num_races:
        time = int(times[i])
        distance = int(distances[i])

        total *= numWins(time, distance)
        i += 1

    return total


def main():
    input_file = "input/d06.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
