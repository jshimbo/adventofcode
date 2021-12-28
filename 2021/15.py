import sys
from heapq import heappush, heappop


def print_board_path(board, path):
    color_path = '\u001b[32;1m'
    color_reset = '\u001b[0m'
    for y, row in enumerate(board):
        line = ''
        for x, c in enumerate(row):
            is_path = (x, y) in path
            if is_path:
                line += color_path
            line += str(c)
            if is_path:
                line += color_reset
        print(line)
    return


def trip_cost(board, path):
    cost = 0
    for (x, y) in path:
        cost += board[y][x]
    return cost


def heuristic(board, next):
    return 0


def get_cost(board, next):
    (x, y) = next
    return int(board[y][x])


def get_neighbors(board, pos):
    (x, y) = pos
    neighbors = []

    height = len(board)
    width = len(board[0])

    for x2 in [x - 1, x + 1]:
        if 0 <= x2 < width:
            neighbors.append((x2, y))
    for y2 in [y - 1, y + 1]:
        if 0 <= y2 < height:
            neighbors.append((x, y2))

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
            if trip_cost(board, path) != result:
                print("Assert failed: g score and path disagree")
                return False
            # path.append(start)
            # print_board_path(board, path)
            return result

        neighbors = get_neighbors(board, current)
        for next in neighbors:
            new_cost = g_score[current] + get_cost(board, next)
            if next not in g_score or new_cost < g_score[next]:
                g_score[next] = new_cost
                priority = new_cost + heuristic(board, next)
                # f score is the best guess cost if we go through this node
                # priority queue includes f_score functionality
                heappush(open_list, (priority, next))
                came_from[next] = current

    # open_list is empty but did not reach goal
    return False


def extend_board(board, size):
    board2 = []
    # extend right size - 1 times
    for _, row in enumerate(board):
        new_row = []
        for s in range(size):
            for _, c in enumerate(row):
                x = c + s
                if x > 9:
                    x = x % 10 + 1
                new_row.append(x)
        board2.append(new_row)
    # next, extend down size -1 times
    new_board = []
    for s in range(size):
        for _, row in enumerate(board2):
            new_row = []
            for _, c in enumerate(row):
                x = c + s
                if x > 9:
                    x = x % 10 + 1
                new_row.append(x)
            new_board.append(new_row)

    return new_board


def main():
    input_file = 'input/15-input-test'
    board = []

    fp = open(input_file if len(sys.argv) <
              2 else sys.argv[1], encoding="utf-8")

    for line in fp:
        board.append(list(map(int, list(line.strip()))))

    start = (0, 0)
    goal = (len(board[0])-1, len(board)-1)

    cost = a_star_search(board, start, goal)

    print("Part 1")
    print("Start", start)
    print("Goal", goal)
    print("Trip cost", cost)

    print("")
    print("Part 2")

    board = extend_board(board, 5)

    start = (0, 0)
    goal = (len(board[0])-1, len(board)-1)

    cost = a_star_search(board, start, goal)

    print("Start", start)
    print("Goal", goal)
    print("Trip cost", cost)


if __name__ == '__main__':
    main()
