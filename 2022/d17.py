# 2022 Day 17: Tetris

import copy


def markCave(cave, rock, x, y):
    for yr in range(len(rock)):  # y-coordinate of the rock
        for xr in range(len(rock[0])):  # x-coordinate of the rock
            yc = y + yr  # y-coordinate for the cave
            xc = x + xr  # x-coordinate for the cave
            if rock[yr][xr] != '.':
                assert cave[yc][xc] != '#'
                cave[yc][xc] = rock[yr][xr]
    return cave


def didCollide(cave, rock, x, y):
    # Returns:
    #   True - yes, we collided
    #   False - no, OK to move there

    # Rocks fall toward y = 0

    result = False
    right_wall = 7

    if x < 0 or x + len(rock[0]) > right_wall:
        # touched a wall
        result = True
    else:
        for yr in range(len(rock)):  # y-coordinate of the rock
            if result:
                break
            for xr in range(len(rock[0])):  # x-coordinate of the rock
                xc = x + xr  # coordinates for the cave
                yc = y + yr
                if rock[yr][xr] != '.' and cave[yc][xc] != '.':
                    result = True
                    break

    return result


def topFloor(cave):
    y = len(cave) - 1
    while y >= 0 and '#' not in cave[y]:
        y -= 1

    if y < 0:
        y = 0

    return y


def extendCave(cave, y):
    # make sure cave is at least y levels tall
    while len(cave) < y:
        cave.append(list("." * 7))
    return cave


def getRocks():
    filename = "input/d17-rocks.txt"
    with open(filename) as f:
        lines = f.read().split("\n\n")

    shapes = []

    for line in lines:
        shape = []
        s2 = line.split("\n")
        for line in s2:
            if line:
                shape.append(list(line))
        s4 = []
        for s3 in reversed(shape):  # align coordinate systems
            s4.append(s3)
        shapes.append(s4)

    return shapes


def solve(lines, num_rocks, part):
    cave = []

    rocks = getRocks()

    level = 0  # no rocks yet
    rock_index = 0  # rocks index
    rock = rocks[rock_index]  # increment index later

    x = 2
    y = level + 3 + len(rock) - 1  # subtract 1 for offset
    cave = extendCave(cave, y + 1)

    puffs = lines[0]
    top_floor = 0
    puffs_index = 0
    fast_forwarded = False
    last_num_rocks_left = num_rocks_left = num_rocks
    cycle_memo = None

    while num_rocks_left > 0:
        if part == 2 and not fast_forwarded and puffs_index == 0:
            last_top_floor = top_floor
            top_floor = topFloor(cave)
            top_floor_delta = top_floor - last_top_floor

            num_rocks_delta = last_num_rocks_left - num_rocks_left
            last_num_rocks_left = num_rocks_left

            if cycle_memo:  # skip the first time through loop
                if all([cycle_memo["floor delta"] == top_floor_delta,
                        cycle_memo["num rocks delta"] == num_rocks_delta,
                        cave[cycle_memo["top floor"]] == cave[top_floor],
                        cycle_memo["rock index"] == rock_index]):
                    num_periods = int(num_rocks_left / num_rocks_delta)
                    add_later = num_periods * top_floor_delta
                    num_rocks_left -= num_periods * num_rocks_delta
                    fast_forwarded = True
                    print("Found repeating cycle. Fast forwarding.")

            cycle_memo = {"rock index": rock_index, "num rocks delta": num_rocks_delta,
                          "top floor": top_floor, "floor delta": top_floor_delta}

        puff = puffs[puffs_index]
        puffs_index += 1
        if puffs_index >= len(lines[0]):
            puffs_index = 0

        # Can we move horizontally?
        assert puff == "<" or puff == ">"
        if puff == "<":
            x_maybe = x - 1
        else:
            x_maybe = x + 1
        if not didCollide(cave, rock, x_maybe, y):
            x = x_maybe  # do not move

        # Can we move vertically?
        if y == 0:
            # on ground floor
            stopped = True
        else:
            # check next level
            y_maybe = y - 1
            stopped = didCollide(cave, rock, x, y_maybe)
            if not stopped:
                y = y_maybe

        if stopped:
            # no more moves
            # 1. Mark it
            cave = markCave(cave, rock, x, y)
            # 2. update high rock mark
            level = topFloor(cave)
            level += 1  # penthouse
            # 3. Get next rock
            rock_index = (rock_index + 1) % len(rocks)
            rock = rocks[rock_index]
            x = 2
            y = level + 3
            cave = extendCave(cave, y + len(rock) + 1)
            # 4. Update rock counter
            num_rocks_left -= 1  # checked at top of loop

    if part == 2:
        level += add_later

    return level


def main():
    filename = "input/d17.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines, num_rocks=2022, part=1))
    print("Part 2:", solve(lines=lines, num_rocks=1000000000000, part=2))


if __name__ == '__main__':
    main()
