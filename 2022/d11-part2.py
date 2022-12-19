import re


def doOperation(item, op, divisor):
    instruction = op.split(" ")

    for factor, modulus in item.items():
        arg1 = modulus
        if instruction[2] == "old":
            arg2 = modulus
        else:
            arg2 = int(instruction[2])
        if instruction[1] == '+':
            answer = arg1 + (arg2 % factor)
        elif instruction[1] == '*':
            answer = arg1 * (arg2 % factor)
        else:
            print("Operator is", instruction[1])
            assert False
        item[factor] = answer % factor

    return item[divisor]


def createMods(i):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    items = {}

    for p in primes:
        items[p] = i % p

    return items


def solve(monkey_progs, part, rounds):
    result = 0

    monkeys = []

    # Setup
    for program in monkey_progs:
        monkey = {}
        lines = program.splitlines()

        # number of times inspected
        monkey['times'] = 0
        # Test
        monkey['name'] = int(re.search(r'\d+', lines[0]).group(0))
        # Starting Items
        monkey['items'] = [createMods(int(i))
                           for i in re.findall(r'\d+', lines[1])]
        # Operation
        monkey['op'] = lines[2].split(':')[1].split('=')[1].strip()
        # Test
        monkey['divisor'] = int(re.search(r'\d+', lines[3]).group(0))
        # if True
        monkey['if_true'] = int(re.search(r'\d+', lines[4]).group(0))
        # if False
        monkey['if_false'] = int(re.search(r'\d+', lines[5]).group(0))

        monkeys.append(monkey)

    for _ in range(rounds):
        for m in monkeys:
            for item in m['items']:
                divisor = m["divisor"]
                worry_level = doOperation(
                    item=item, op=m["op"], divisor=divisor)
                m['times'] += 1

                # if part == 1:
                #     worry_level = int(worry_level/3)

                if worry_level % divisor == 0:
                    dest_num = m['if_true']
                else:
                    dest_num = m['if_false']
                monkeys[dest_num]['items'].append(item)
            m['items'] = []  # clear work queue

    # get result
    top_two = []
    for m in monkeys:
        top_two.append(m['times'])
    top_two = sorted(top_two, reverse=True)
    result = top_two[0] * top_two[1]

    return result


def main():
    filename = "input/d11.txt"
    with open(filename) as f:
        monkey_progs = f.read().split("\n\n")

    print("Part 2:", solve(monkey_progs=monkey_progs, part=2, rounds=10000))


if __name__ == '__main__':
    main()
