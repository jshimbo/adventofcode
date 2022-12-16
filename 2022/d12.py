import sys
from heapq import heappush, heappop


def printPage(page):
    for line in page:
        raster = ''.join(line)
        print(raster)


def printMap(board, path, start, goal):
    color_on = '\u001b[32;1m'
    color_off = '\u001b[0m'

    # init map
    chart = []
    for row in board:
        chart.append(list(row))

    steps = reversed(path)
    prev = start
    hit_goal = 0
    hit_start = 0

    for current in steps:
        (x2, y2) = current
        (x1, y1) = prev

        chart[y1][x1] = color_on + chart[y1][x1] + color_off

        if current == start:
            hit_start += 1
        elif current == goal:
            hit_goal += 1
        if y1 != y2 and x1 != x2:
            print("Error: Moved diagonally")

        prev = current

    printPage(chart)
    if hit_goal > 1:
        print("Error: Reached goal more than once")
    if hit_start > 0:
        print("Warning: Returned to start", hit_start, "times")
    return True


def heuristic(board, next):
    return 0


def get_neighbors(board, pos):
    (x, y) = pos
    neighbors = []

    height = len(board)
    width = len(board[0])

    if board[y][x] == 'S':
        elevation = ord('a')
    else:
        elevation = ord(board[y][x])

    # up, down, right, left
    for pos in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
        (x2, y2) = pos
        if 0 <= x2 < width and 0 <= y2 < height:
            if board[y2][x2] == 'E':
                elev2 = ord('z')
            else:
                elev2 = ord(board[y2][x2])
            if elev2 < (elevation + 2):
                neighbors.append((x2, y2))

    return neighbors


# reconstruct_path() and a_star_search() are from
# https://www.redblobgames.com/pathfinding/a-star/implementation.html
# Modifications from Wikipedia article on A*


def reconstruct_path(came_from, start, goal):
    # backwards
    current = goal
    path = []
    while current != start:
        path.append(current)
        try:
            current = came_from[current]
        except:
            print(current)
            raise
    # path.append(start) # start is ignored in path cost
    # path.reverse() # unnecessary
    return path


def a_star_search(board, start, goal):
    open_list = []
    heappush(open_list, (0, start))

    # list of steps on path taken
    came_from = {}
    came_from[start] = None

    # g score is cheapest known path from start to node
    # redblobgames.com calls this cost_so_far
    g_score = {}
    g_score[start] = 0

    while len(open_list) != 0:
        current = heappop(open_list)[1]
        if current == goal:
            result = g_score[goal]

            # check result against path
            path = reconstruct_path(came_from, start, goal)

            # g score and path must agree
            assert len(path) == result
            # print(path)
            # printMap(board, path, start, goal)

            # assert trip_cost(board, path) == result
            # path.append(start)
            # print_board_path(board, path)

            return result

        neighbors = get_neighbors(board, current)
        for next in neighbors:
            new_cost = g_score[current] + 1
            if next not in g_score or new_cost < g_score[next]:
                g_score[next] = new_cost
                priority = new_cost + heuristic(board, next)
                # f score is the best guess cost if we go through this node
                # priority queue includes f_score functionality
                heappush(open_list, (priority, next))
                came_from[next] = current
                # print("g_score:", g_score)

    # open_list is empty but did not reach goal
    return False


def findAll(board, s):
    result = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] in s:
                result.append((x, y))
    return result


def findStart(board, c):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == c:
                return (x, y)
    return None


def solve2(board):
    steps = 9999
    start_list = findAll(board, 'aS')
    goal = findStart(board, 'E')
    assert start_list
    assert goal

    for start in start_list:
        s = a_star_search(board, start, goal)
        if s and s < steps:
            steps = s

    return steps


def solve1(board):
    steps = 0
    start = findStart(board, 'S')
    goal = findStart(board, 'E')
    assert start
    assert goal
    steps = a_star_search(board, start, goal)
    return steps


def main():
    filename = 'input/d12-pre'
    filename = "input/d12.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve1(board=lines))
    print("Part 2:", solve2(board=lines))


if __name__ == '__main__':
    main()
