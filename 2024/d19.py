from heapq import heappush, heappop


def heuristic(a, b):
    return abs(a - b)


def get_neighbors(towel: str, i, colors):
    neighbors = []

    for color in colors:
        if towel[i::].startswith(color):
            neighbors.append(i + len(color))

    return neighbors


# reconstruct_path() and a_star_search() are from
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
# Modifications from Wikipedia article on A*


def a_star_search(towel, start, goal, colors):
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

        neighbors = get_neighbors(towel, current, colors)
        for next in neighbors:
            new_cost = next
            if next not in g_score or new_cost < g_score[next]:
                g_score[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                heappush(open_list, (priority, next))
                came_from[next] = current

    return came_from


def solve(lines):
    colors = []
    score = 0
    for i, line in enumerate(lines):
        if i == 0:
            colors = list([x.strip() for x in line.split(",")])
        elif i > 1:
            towel = line.strip()
            start = 0
            goal = len(towel)
            came_from = a_star_search(towel, start, goal, colors)
            if goal in came_from.keys():
                score += 1

    return score


def main():
    input_file = "input/d19.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines))


if __name__ == "__main__":
    main()
