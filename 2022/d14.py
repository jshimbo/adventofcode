# Day 14: Regolith Reservoir (falling sand)

import copy


def caveDimensions(cave):
    min_x = 99999
    max_x = 0
    max_y = 0
    for key, value in cave.items():
        x = min(value)
        if x < min_x:
            min_x = x
        x = max(value)
        if x > max_x:
            max_x = x
        if key > max_y:
            max_y = key
    return {"min_x": min_x, "max_x": max_x, "max_y": max_y}


def displayCave(ascii_cave):
    # output to terminal
    max_y = 0
    keys = ascii_cave.keys()

    color_on = '\u001b[32m'
    color_off = '\u001b[0m'

    for key, value in ascii_cave.items():
        for i in range(len(value)):
            if value[i] == '#':
                value[i] = color_on + '#' + color_off

    for key in keys:
        if key > max_y:
            max_y = key

    for y in range(max_y+1):
        if y in keys:
            print("".join(ascii_cave[y]), y)
        else:
            print("")


def printCave(cave, rocks):
    dimensions = caveDimensions(cave)
    min_x = dimensions["min_x"]
    max_x = dimensions["max_x"]

    new_cave = {}
    for key in cave.keys():
        input = cave[key]
        output = []
        for _ in range(min_x, max_x + 1):
            output.append(" ")
        for x in input:
            output[x-min_x] = 'o'
        new_cave[key] = output

    # Add sand spigot
    output = []
    for _ in range(min_x, max_x + 1):
        output.append(" ")
    output[500-min_x] = '+'
    new_cave[0] = output

    if rocks:
        # overlay original maze
        for key in rocks.keys():
            input = rocks[key]
            for x in input:
                new_cave[key][x-min_x] = '#'

    displayCave(ascii_cave=new_cave)  # output to terminal


def digCave(lines):
    cave = {}
    for line in lines:
        last_pos = None
        coords = line.split(' -> ')
        for c in coords:
            tmp = c.split(',')
            x = int(tmp[0])
            y = int(tmp[1])
            if not y in cave:
                cave[y] = []

            if last_pos:
                x0, y0 = last_pos
                last_pos = (x, y)
                if y0 == y:
                    if x0 > x:
                        # swap
                        (x, x0) = (x0, x)
                    for i in range(x0, x+1):
                        cave[y].append(i)
                else:  # x0 == x
                    if y0 > y:
                        # swap
                        (y, y0) = (y0, y)
                    for i in range(y0, y+1):
                        if not i in cave:
                            cave[i] = []
                        cave[i].append(x)
            else:
                last_pos = (x, y)

        fresh_cave = {}
        for key in cave.keys():
            fresh_cave[key] = set(cave[key])
    return fresh_cave


def blocked(sand, cave):
    x, y = sand
    result = False
    next_y = y + 1

    if next_y in cave:
        next_row = cave[next_y]
        xs = set([x, x-1, x+1])
        result = xs.issubset(next_row)

    return result


def solve(lines, part):
    # create cave
    cave = digCave(lines)

    # save orignal cave so we can overlay the rocks later
    # orig_cave = copy.deepcopy(cave)

    dimensions = caveDimensions(cave)
    floor = dimensions["max_y"]

    # print("Cave dimensions are", dimensions)

    grains = 0  # grains of sand
    spigot = (500, 0)
    stopped = False
    victory = False
    # for each grain of sand
    while not victory:
        sand = spigot
        grains += 1

        if part == 2 and blocked(sand, cave):
            victory = True

        # Make one move
        while not (stopped or victory):
            (x, y) = sand
            # check next row
            next_y = y + 1
            if next_y > floor and part == 1:
                victory = True
                grains -= 1
            elif next_y > floor + 1:  # tacit part 2
                stopped = True
            elif not next_y in cave:
                # Level is empty
                # Go down one and continue
                sand = (x, next_y)
            else:
                next_row = cave[next_y]
                if not x in next_row:
                    sand = (x, next_y)
                elif not x-1 in next_row:
                    sand = (x-1, next_y)
                elif not x+1 in next_row:
                    sand = (x+1, next_y)
                else:
                    stopped = True

        if sand == (500, 0):
            victory = True
            stopped = False

        # We can go no further, mark our spot
        if stopped:
            stopped = False
            (x, y) = sand
            sand = None
            if y in cave:
                assert x not in cave[y]
                cave[y].add(x)
            else:
                # First item in this level
                cave[y] = set([x])  # fill it

    # printCave(cave, rocks=orig_cave)
    return grains


def main():
    filename = "input/d14.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines, part=1))
    print("Part 2:", solve(lines=lines, part=2))


if __name__ == '__main__':
    main()
