def get_operand(patch_cords, registers, prog, key):
    op = prog[key]
    if op in registers:
        return registers[op]
    else:
        return apply(patch_cords, registers, op)


def apply(patch_cords, registers, reg):
    prog = patch_cords[reg]

    op1 = get_operand(patch_cords, registers, prog, "op1")
    op2 = get_operand(patch_cords, registers, prog, "op2")
    opcode = prog["opcode"]

    ops = {
        "AND": op1 and op2,
        "OR": op1 or op2,
        "XOR": op1 ^ op2,
    }
    return ops[opcode]


def solve(lines):
    setting_up_registers = True
    registers = {}
    patch_cords = {}
    z_reg = set()
    result = 0
    for line in lines:
        line = line.strip()
        if not line:
            setting_up_registers = not setting_up_registers
        elif setting_up_registers:
            reg, s = line.split(":")
            registers[reg] = int(s)
        else:
            r1, op, r2, _, res = line.split()
            assert res not in patch_cords
            patch_cords[res] = {"opcode": op, "op1": r1, "op2": r2}
            if res[:1] == "z":
                z_reg.add(res)
                registers[res] = 0

    for exp, z in enumerate(sorted(list(z_reg))):
        res = apply(patch_cords, registers, z)
        if res == True:
            result += 2**exp * res

    print("Answer to part 1:", result)


def main():
    input_file = "input/d24.txt"

    with open(input_file) as f:
        lines = f.readlines()

    solve(lines)


if __name__ == "__main__":
    main()
