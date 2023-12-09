import queue


def solve(lines, part):
    total = 0

    for l in lines:
        q = queue.LifoQueue()
        dataset = [int(e) for e in l.split()]
        q.put(dataset)

        done = False
        while not done:
            dataset = [dataset[i + 1] - dataset[i] for i in range(len(dataset) - 1)]
            q.put(dataset)
            done = all(i == 0 for i in dataset)

        q.get()  # discard the zeros
        delta = 0  # the first delta is always zero

        while not q.empty():
            dataset = q.get()
            if part == 1:
                delta = dataset[-1] + delta
            else:
                delta = dataset[0] - delta

        total += delta

    return total


def main():
    input_file = "input/d09.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    print("Answer to part 1:", solve(lines, part=2))


if __name__ == "__main__":
    main()
