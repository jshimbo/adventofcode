# Day 23: Unstable Diffusion


def getScore(elves):

    min_y = min_x = 99999999
    max_y = max_x = 0

    num_elves = 0

    for y, row in elves.items():
        if len(row) > 0:
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            for x in row.keys():
                num_elves += 1
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    print(f"Reconfirming {num_elves} found")
    score = width * height - num_elves
    return score


def applyMoves(elves, moves):
    update_list = {}

    # for each row
    for y2, row in moves.items():
        # updated elves
        # for i in [y2-1, y2, y2+1]:
        #     if i not in update_list:
        #         update_list[i] = {}
        if y2 not in update_list:
            update_list[y2] = {}

        # for each move in this row
        for x2, move in row.items():
            if not move["dup"]:
                # get elf
                prev_x = move["prev_x"]
                prev_y = move["prev_y"]
                elf = elves[prev_y][prev_x]
                # paranoid cleanup
                elf["prev_x"] = elf["prev_y"] = None
                # move elf update list
                update_list[y2][x2] = elf
                del elves[prev_y][prev_x]  # delete old

    # add update_list to elves
    for y2, row in update_list.items():
        if len(row) > 0 and not y2 in elves:
            elves[y2] = {}

        for x2, elf in row.items():
            assert not x2 in elves[y2]
            elves[y2][x2] = elf

    return elves


def is_isolated(elves, x, y):
    for y2 in [y+1, y-1]:
        if y2 in elves:
            row = elves[y2]
            if x-1 in row or x in row or x+1 in row:
                return False

    row = elves[y]
    if x-1 in row or x+1 in row:
        return False

    return True


def check_if_open(elves, x, y):
    if y in elves and x in elves[y]:
        return False  # an elf is already here
    return True


def getMoves(elves, direction):
    compass = ["N", "S", "W", "E"]
    moves = {}
    elf_count = 0
    move_count = 0

    dir_list = []
    for i in range(len(compass)):
        dir_list.append(compass[(direction + i) % len(compass)])

    for y, row in elves.items():
        for x, elf in row.items():
            elf_count += 1

            move_recorded = False

            # do not move if completely isolated
            if is_isolated(elves, x, y):
                continue  # next elf, please

            for dir in dir_list:
                if move_recorded:
                    break

                if dir == "N" or dir == "S":
                    if dir == "N":
                        y2 = y - 1  # North
                    else:
                        y2 = y + 1  # South

                    num_open = 0
                    for i in (x, x+1, x-1):
                        if check_if_open(elves=elves, x=i, y=y2):
                            num_open += 1
                    if num_open == 3:
                        move_recorded = True
                        if y2 in moves and x in moves[y2]:
                            moves[y2][x]["dup"] = True
                        else:
                            if not y2 in moves:  # does row exist?
                                moves[y2] = {}
                            moves[y2][x] = {"name": elf["name"], "prev_x": x,
                                            "prev_y": y, "dup": False}

                            move_count += 1

                else:  # "E" or "W"
                    if dir == "W":
                        x2 = x - 1  # West
                    else:
                        x2 = x + 1  # East
                    num_open = 0
                    for y2 in [y, y-1, y+1]:
                        if check_if_open(elves=elves, x=x2, y=y2):
                            num_open += 1
                    if num_open == 3:
                        move_recorded = True
                        if y in moves and x2 in moves[y]:
                            moves[y][x2]["dup"] = True
                        else:
                            if not y in moves:  # does row exist
                                moves[y] = {}
                            moves[y][x2] = {"name": elf["name"],
                                            "prev_x": x, "prev_y": y, "dup": False}
                            move_count += 1

    return moves


def setupElves(lines):
    elves = {}
    y = 0
    name = 0
    for line in lines:
        x = 0
        for c in line:
            if c == '#':
                if not y in elves:
                    elves[y] = {}
                elves[y][x] = ({"name": name})
                name += 1
            x += 1
        y += 1

    print(name, "elves found")
    return elves


def solve(lines, part):
    elves = setupElves(lines)

    direction = 0  # 0 = north

    if part == 1:
        rounds = 10
        for _ in range(rounds):
            moves = getMoves(elves, direction)
            direction = (direction + 1) % 4
            if len(moves) > 0:
                elves = applyMoves(elves, moves)

        result = getScore(elves)
    else:
        moves = {"fake": True}
        num_rounds = 0
        while len(moves) > 0:
            num_rounds += 1
            moves = getMoves(elves, direction)
            direction = (direction + 1) % 4
            if len(moves) > 0:
                elves = applyMoves(elves, moves)

        result = num_rounds

    return result


def main():
    filename = "input/d23.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines, part=1))
    print("Part 2:", solve(lines=lines, part=2))


if __name__ == '__main__':
    main()
