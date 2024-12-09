def initDisk(line):
    disk = []
    space = False
    value = 0
    for c in list(line):
        count = int(c)
        while count > 0:
            if space:
                disk.append(".")
            else:
                disk.append(str(value))
            count -= 1
        space = not space
        if space:
            value += 1
    return disk


def defrag1(disk):
    left = 0
    right = len(disk) - 1
    new_disk = []
    while left <= right:
        if disk[left] == ".":
            while disk[right] == ".":
                right -= 1
            new_disk.append(disk[right])
            right -= 1
        else:
            new_disk.append(disk[left])
        left += 1

    return new_disk


def solve1(line):
    # Input is one stripped line
    disk = initDisk(line)
    disk = defrag1(disk)

    total = 0
    for i, c in enumerate(disk):
        total += i * int(c)
    return total


def main():
    input_file = "input/d09.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines[0].strip()))
    # print("Answer to part 2:", solve2(lines[0].strip()))


if __name__ == "__main__":
    main()
