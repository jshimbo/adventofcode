import re


def getCombo(registers, operand):
    result = 0
    if 0 <= operand < 4:
        result = operand
    elif operand == 4:
        result = registers["A"]
    elif operand == 5:
        result = registers["B"]
    elif operand == 6:
        result = registers["C"]
    else:
        print("invalid operand")
        print(registers)
        exit()
    return result


def executeOp(opcode, operand, registers):
    output = None
    no_increment = False
    if opcode == 0:  # adv
        operand = getCombo(registers, operand)
        registers["A"] = registers["A"] // (2**operand)
    elif opcode == 1:  # bxl
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:  # bst
        operand = getCombo(registers, operand)
        registers["B"] = operand % 8
    elif opcode == 3:  # jnz
        if registers["A"] != 0:
            registers["PC"] = operand
            no_increment = True
    elif opcode == 4:  # bxc
        registers["B"] ^= registers["C"]
    elif opcode == 5:  # out
        operand = getCombo(registers, operand)
        output = operand % 8
    elif opcode == 6:  # bdv
        operand = getCombo(registers, operand)
        registers["B"] = registers["A"] // (2**operand)
    elif opcode == 7:  # cdv
        operand = getCombo(registers, operand)
        registers["C"] = registers["A"] // (2**operand)
    else:
        print("Unimplemented instruction")
        print(registers)
        exit()

    if no_increment:
        no_increment = not no_increment
    else:
        registers["PC"] += 2

    return registers, output


def solve(lines):
    output = []
    registers_complete = False
    registers = {"PC": 0}
    for line in lines:
        line = line.strip()
        if not registers_complete:
            parts = re.match(r"Register ([A-Z]): (\d+)", line)
            if parts == None:
                registers_complete = True
            else:
                registers[parts[1]] = int(parts[2])
        else:
            parts = line.split(":")
            if len(parts) > 1:
                program = [int(x) for x in parts[1].split(",")]

    registers["PC"] = 0
    while registers["PC"] < len(program) - 1:
        opcode = int(program[registers["PC"]])
        operand = int(program[registers["PC"] + 1])
        registers, out = executeOp(opcode, operand, registers)
        if out != None:
            output.append(str(out))

    return ",".join(output)


def main():
    filename = "input/d17.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines))


if __name__ == "__main__":
    main()
