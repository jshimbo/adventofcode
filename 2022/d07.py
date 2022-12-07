def du(root):
    result = root['size']
    for child in root['children']:
        result += du(child)
    return result


def findFreespace(node, goal, candidate):
    x = du(node)
    if x >= goal and x < candidate:
        candidate = x

    for child in node['children']:
        candidate = findFreespace(child, goal, candidate)

    return candidate


def freespace(node, capacity, needed):
    usage = du(node)
    freespace = capacity - usage
    goal = needed - freespace  # how much more needed

    return findFreespace(node, goal, usage)


def getSum(node, maximum):
    total = 0

    x = du(node)
    if x <= maximum:
        total += x

    for child in node['children']:
        total += getSum(node=child, maximum=maximum)

    return total


def solve(lines, part):
    dir_stack = []
    root = {'name': '/', 'size': 0, 'children': []}
    pwd = root
    answer = 0

    for l in lines:
        line = l.split(' ')

        if line[0] == '$':
            # new cmd
            cmd = line[1]
            if cmd == 'cd':
                # chdir
                dest = line[2]
                if dest == "/":
                    pwd = root
                    dir_stack = []
                elif dest == '..':
                    pwd = dir_stack.pop()
                else:
                    dir_stack.append(pwd)

                    found = False
                    for n in pwd['children']:
                        if n['name'] == dest:
                            pwd = n
                            found = True
                            break

                    if not found:
                        # dir not found
                        new_node = {'name': dest, 'size': 0,
                                    'children': []}
                        pwd['children'].append(new_node)
                        pwd = new_node

        else:
            # not a new cmd so it must be inside an ls cmd
            s = line[0]
            if s.isnumeric():
                # it's a file size
                pwd['size'] += int(s)
            else:
                # it's a dir
                pass

    if part == 1:
        answer = getSum(node=root, maximum=100000)
    else:
        answer = freespace(node=root, capacity=70000000, needed=30000000)
    return answer


def main():
    # input_file = "input/d07-pre"
    input_file = "input/d07"
    with open(input_file) as f:
        lines = f.read().splitlines()

    print("Answer to part 1:", solve(lines, 1))
    print("Answer to part 2:", solve(lines, 2))


if __name__ == '__main__':
    main()
