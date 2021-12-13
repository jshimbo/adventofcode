def search_sheet(sheet, dot):
    for _, row in enumerate(sheet):
        if row[0] == dot[0] and row[1] == dot[1]:
            return dot
    return False


def print_paper(sheet):
    rows = 7
    cols = 40
    content = [[" "]*cols for _ in range(rows)]

    for dot in sheet:
        x, y = dot
        content[y][x] = '#'

    print("")
    for i in range(rows):
        for j in range(cols):
            print(content[i][j], end="")
        print("")
    print("")
    return


def fold(paper, instruction):
    axis = instruction[0]
    crease = instruction[1]

    new_sheet = []
    for dot in paper:
        x, y = dot
        if axis == "y":
            new_x = x
            if y > crease:
                new_y = crease - abs(y - crease)
            else:
                new_y = y

        if axis == "x":
            new_y = y
            if x > crease:
                new_x = crease - abs(x-crease)
            else:
                new_x = x

        new_dot = tuple([new_x, new_y])
        if search_sheet(new_sheet, new_dot) == False:
            new_sheet.append(new_dot)

    print(len(new_sheet), "dots after folding along", axis, "=", crease)

    return new_sheet


def part1(sheet, instructions):
    for instruction in instructions:
        sheet = fold(sheet, instruction)
    return sheet


def main():
    input_file = "input/13-input"
    clean_sheet = []
    folding_instructionss = []

    input_part = 1
    with open(input_file) as fp:
        for line in fp:
            line = line.strip()

            if not line:
                # start reading folding instructions
                input_part += 1
            elif input_part == 1:
                clean_sheet.append(tuple(map(int, line.split(','))))
            elif input_part == 2:
                tmp = line.split(" ")[2].split('=')
                folding_instructionss.append([tmp[0], int(tmp[1])])

    answer1 = part1(clean_sheet, folding_instructionss)
    print_paper(answer1)


if __name__ == '__main__':
    main()
