def begins_with(path, letter):
    node: str
    for node in path:
        if node.startswith(letter):
            return True
    return False


def find_all_paths(graph, start, goal, path=[], cost=2):
    path = path + [start]  # concatenate two lists

    if cost == 0:
        return [path] if goal in graph[start] else []

    # return all paths
    return [
        newpath
        for node in graph[start]
        if node not in path
        for newpath in find_all_paths(graph, node, goal, path, cost - 1)
    ]


def solve(lines):
    edges = [line.strip().split("-") for line in lines]

    graph = {}
    for p1, p2 in edges:
        graph.setdefault(p1, []).append(p2)
        graph.setdefault(p2, []).append(p1)

    cycles = set()
    for k in graph.keys():
        path_array = find_all_paths(graph, start=k, goal=k)
        for p in path_array:
            if begins_with(p, "t"):
                cycles.add(tuple(sorted(p)))

    print("Answer to part 1:", len(cycles))


def main():
    input_file = "input/d23.txt"

    with open(input_file) as f:
        lines = f.readlines()

    solve(lines)


if __name__ == "__main__":
    main()
