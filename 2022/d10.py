def print_screen(screen):
    for row in screen:
        print(row)


def set_pixel(cycle_count, sprite_pos):
    result = '.'
    if abs(cycle_count % 40 - sprite_pos) < 2:
        result = '#'
    return result


def solve2(program):
    cycle_count = 0
    pc = 0  # program counter
    x_reg = 1

    rows = 6
    row_len = 40
    screen = []

    mid_instruction = False
    arg = 0

    for _ in range(rows):
        row = ''
        for _ in range(row_len):
            if mid_instruction:
                # addx instruction takes two cycles
                row += set_pixel(cycle_count=cycle_count,
                                 sprite_pos=x_reg)
                x_reg += arg
                mid_instruction = False
            else:
                instruction = program[pc].split(' ')
                pc += 1

                if instruction[0] == 'addx':
                    row += set_pixel(cycle_count=cycle_count,
                                     sprite_pos=x_reg)
                    arg = int(instruction[1])
                    mid_instruction = True
                else:
                    # noop
                    row += set_pixel(cycle_count=cycle_count,
                                     sprite_pos=x_reg)
            cycle_count += 1

        screen.append(row)

    return screen


def it_is_time(count):
    result = False
    if count < 221 and (count - 20) % 40 == 0:
        result = True
    return result


def solve1(program):
    result = 0
    cycle_count = 0
    x_reg = 1

    for p in program:
        instructions = p.split(' ')
        if instructions[0] == 'addx':
            for _ in range(2):
                cycle_count += 1
                if it_is_time(cycle_count):
                    result += x_reg * cycle_count
            x_reg += int(instructions[1])
        else:
            # noop
            cycle_count += 1
            if it_is_time(cycle_count):
                result += x_reg * cycle_count

    return result


def main():
    input_file = 'input/d10.txt'

    with open(input_file) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve1(program=lines))
    print("Part 2:")
    result = solve2(program=lines)
    print_screen(result)


if __name__ == '__main__':
    main()
