import re


def printShip(ship):
    str = ""
    deck_num = 1
    for deck in ship:
        str = "  ".join(deck)
        print(str, ": ", deck_num)
        deck_num += 1


def zip_char_array(dest, src):
    for x in range(len(dest)):
        if dest[x] == ' ':
            dest[x] = src[x]
    return dest


def getAnswer(ship):
    top_crates = []
    for _ in range(len(ship[0])):
        top_crates.append(' ')

    for deck in ship:
        top_crates = zip_char_array(top_crates, deck)

    answer = "".join(top_crates)
    return answer


def addDecks(ship, num):
    new_ship = []
    count = 0
    for _ in range(num):
        # create a blank deck and initialize
        new_deck = []
        for _ in range(len(ship[0])):
            new_deck.append(' ')

        new_ship.append(new_deck)

    ship = new_ship + ship
    return ship


def moveCrates(ship, cnt, src, dest, crane_model):

    if cnt > len(ship):
        print("Error: count is ", cnt, " but ship height is ", len(ship))

    # pick crates
    cache = []
    count = cnt
    for deck in ship:
        if deck[src-1] != ' ':
            cache.append(deck[src-1])
            deck[src-1] = ' '
            count -= 1
        if count < 1:
            break

    # find top of dest and add decks if needed
    dest_floor = 0  # 0 is top of ship
    for deck in ship:
        if deck[dest-1] == ' ':
            dest_floor += 1
        else:
            break

    if dest_floor < cnt:
        delta = cnt - dest_floor
        ship = addDecks(ship, delta)
        dest_floor += delta

    # place crates
    if crane_model == 9000:
        y = dest_floor - 1
        # print("Moving", cache, "from", src, "to", dest, "row ", y + 1)
        for c in cache:
            ship[y][dest-1] = c
            y -= 1
    else:
        y = dest_floor - cnt
        # print("Moving", cache, "from", src, "to", dest, "row ", y + 1)
        for c in cache:
            ship[y][dest-1] = c
            y += 1

    return ship


def solve(crates_s, moves_s, crane_model):

    lines = crates_s.splitlines()
    ship = []
    for l in lines:
        width = len(l)
        layer = []
        for x in range(1, width, 4):
            c = l[x]
            layer.append(c)
        ship.append(layer)
        layer = []

    ship.pop()

    lines = moves_s.splitlines()
    for l in lines:
        x = re.findall(r'\d+', l)
        cnt = int(x[0])
        src = int(x[1])
        dest = int(x[2])
        ship = moveCrates(ship, cnt, src, dest, crane_model)

    # printShip(ship)
    return getAnswer(ship)


def main():
    filename = "input/d05"
    with open(filename) as f:
        data_parts = f.read().split("\n\n")

    print("Part 1:", solve(data_parts[0], data_parts[1], 9000))
    print("Part 1:", solve(data_parts[0], data_parts[1], 9001))


if __name__ == '__main__':
    main()
