from heapq import heappush, heappop


def printMap(m):
    for row in m:
        print("".join([str(x) for x in row]))


def printMapPath(m, path):
    color_path = "\u001b[32;1m"
    color_reset = "\u001b[0m"
    for y, row in enumerate(m):
        line = ""
        for x, c in enumerate(row):
            is_path = (y, x) in path
            if is_path:
                line += color_path
                line += "O"
            else:
                line += c
            if is_path:
                line += color_reset
        print(line)
    return


def makeMemorySpace(lines, bytes, height, width):
    memory_space = []
    for _ in range(height):
        memory_space.append(list("." * width))

    for i in range(bytes):
        x, y = map(int, lines[i].strip().split(","))
        memory_space[y][x] = "#"

    return memory_space


def heuristic(a, b):
    (y1, x1) = a
    (y2, x2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(memory_space, pos):
    (y, x) = pos
    neighbors = []

    height = len(memory_space)
    width = len(memory_space[0])

    for x2 in [x - 1, x + 1]:
        if 0 <= x2 < width and memory_space[y][x2] != "#":
            neighbors.append((y, x2))
    for y2 in [y - 1, y + 1]:
        if 0 <= y2 < height and memory_space[y2][x] != "#":
            neighbors.append((y2, x))

    return neighbors


# reconstruct_path() and a_star_search() are from
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
# Modifications from Wikipedia article on A*


def reconstruct_path(came_from, start, goal):
    current = goal  # Go backwards from goal
    path = []
    while current != start:
        path.append(current)
        try:
            current = came_from[current]
        except:
            print(current)
            raise
    # path.append(start) # start is not part of cost
    return path


def a_star_search(memory_space, start, goal):
    open_list = []
    heappush(open_list, (0, start))

    # list of steps on path taken
    came_from = {}
    came_from[start] = None

    # g score is cheapest known path from start to node
    # redblobgames.com calls this cost_so_far
    g_score = {}
    g_score[start] = 0

    while len(open_list) > 0:
        current = heappop(open_list)[1]
        if current == goal:
            break

        neighbors = get_neighbors(memory_space, current)
        for next in neighbors:
            new_cost = g_score[current] + 1
            if next not in g_score or new_cost < g_score[next]:
                g_score[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                heappush(open_list, (priority, next))
                came_from[next] = current

    # return came_from, g_score
    return came_from


def solve(lines, part):
    height = 71
    width = 71
    bytes = 1024

    memory_space = makeMemorySpace(lines, bytes, height, width)

    start = (0, 0)
    goal = (height - 1, width - 1)

    if part == 1:
        came_from = a_star_search(memory_space, start, goal)
        path = reconstruct_path(came_from, start, goal)
        return len(path)

    # else Part 2

    # Can we avoid some work?
    i = (len(lines) - bytes) // 2 + bytes
    memory_space = memory_space = makeMemorySpace(lines, i, height, width)
    came_from = a_star_search(memory_space, start, goal)
    if goal not in came_from:
        # Answer is in the first half
        i = bytes - 1
        memory_space = memory_space = makeMemorySpace(lines, i, height, width)

    while i < len(lines):
        came_from = a_star_search(memory_space, start, goal)
        if goal not in came_from:
            x, y = map(int, lines[i].strip().split(","))
            return str(x) + "," + str(y)
        else:
            i += 1
            x, y = map(int, lines[i].strip().split(","))
            memory_space[y][x] = "#"


def main():
    input_file = "input/d18.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    print("Answer to part 2:", solve(lines, part=2))


if __name__ == "__main__":
    main()
