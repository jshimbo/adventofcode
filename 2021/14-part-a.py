import sys

"""
I now know that using linked lists
here was suboptimal.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data, end='')
            printval = printval.next
        print('')


def tally_polymer(polymer):
    tally = {}
    p = polymer.headval
    while p is not None:
        c = p.data
        tally[c] = tally.get(c, 0) + 1
        p = p.next
    return tally


def part1(root, rules):
    prev_ptr = root.headval
    ptr = prev_ptr.next
    while ptr is not None:
        pair = prev_ptr.data + ptr.data
        nucleotide = rules[pair]
        # create node
        new_node = Node(nucleotide)
        # insert node between prev and current ptr
        new_node.next = ptr
        prev_ptr.next = new_node
        prev_ptr = ptr
        ptr = ptr.next

    return root


def main():
    input_file = 'input/14-input'
    rules = {}
    steps = 10
    root = SLinkedList()

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        steps = int(sys.argv[2])
    with open(input_file, encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                pass
            elif not root.headval:
                necleotides = list(line)
                for n in necleotides:
                    ptr = Node(n)
                    if root.headval == None:
                        root.headval = ptr
                    else:
                        prev.next = ptr
                    prev = ptr
            else:
                r = line.split(" -> ")
                rules[r[0]] = r[1]

        poly1 = root
        for _ in range(steps):
            poly1 = part1(poly1, rules)

        tally = tally_polymer(poly1)
        print(tally)
        values = tally.values()
        answer1 = max(values) - min(values)
        print('Answers:')
        print('  Part 1', answer1)


if __name__ == '__main__':
    main()
