import re


def solve(monkey_progs):
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
        monkey['items'] = [int(i) for i in re.findall(r'\d+', lines[1])]
        # Operation
        monkey['op'] = lines[2].split(':')[1].split('=')[1].strip()
        # Test
        monkey['divisor'] = int(re.search(r'\d+', lines[3]).group(0))
        # if True
        monkey['if_true'] = int(re.search(r'\d+', lines[4]).group(0))
        # if False
        monkey['if_false'] = int(re.search(r'\d+', lines[5]).group(0))

        monkeys.append(monkey)

    for _ in range(20):
        for m in monkeys:
            for item in m['items']:
                m['times'] += 1
                old = item  # set up for the eval in the next step
                worry_level = eval(m['op'])
                worry_level = int(worry_level/3)
                if worry_level % m['divisor'] == 0:
                    dest_num = m['if_true']
                else:
                    dest_num = m['if_false']
                monkeys[dest_num]['items'].append(worry_level)
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

    print("Part 1:", solve(monkey_progs))


if __name__ == '__main__':
    main()
