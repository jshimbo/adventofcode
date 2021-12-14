import sys

# Thanks to:
# https://twitter.com/_alelouis/status/1469971001802960903
# https://github.com/fizbin/aoc2021/blob/main/aoc12.py


def find_paths(cave, graph, counts, max_visits):

    ncounts = dict(counts)  # shallow copy

    if cave == 'end':
        # Success. One point.
        return 1

    if cave.islower():
        ncounts[cave] += 1
        if ncounts[cave] > max_visits:
            # Too many visits to this cave
            return 0

        # End of part 1
        # The following code runs fast enough in part 1
        # that we can leave it alone
        how_many_twos = 0
        for c in ncounts:
            if ncounts[c] >= 2 and c.islower():
                how_many_twos += 1

                if how_many_twos > 1:
                    # This is the second cave with two visits.
                    return 0

    return sum([find_paths(next_cave, graph, ncounts, max_visits) for next_cave in graph[cave]])


def main():
    input_file = 'input/12-input'
    counts = {}
    graph = {}

    with open(input_file if len(sys.argv) < 2 else sys.argv[1], encoding="utf-8") as fp:
        for line in fp:
            a, b = tuple(line.strip().split('-'))
            graph[a] = {b} if a not in graph else graph[a].union({b})
            graph[b] = {a} if b not in graph else graph[b].union({a})
            if a.islower():
                counts[a] = 0
            if b.islower():
                counts[b] = 0

    for way in graph.keys():
        graph[way].discard('start')

    answer1 = find_paths('start', graph, counts, 1)
    answer2 = find_paths('start', graph, counts, 2)

    print('Answers:')
    print('  Part 1', answer1)
    print('  Part 2', answer2)


if __name__ == '__main__':
    main()
