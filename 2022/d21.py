# Day 21: Monkey Math
#
# In retrospect, did not need to separate nodes and leaves

def reverseCalc(operator, goal, r, human_is_left):
    if operator == '+':
        answer = goal - r
    elif operator == '*':
        answer = goal / r
    elif operator == '-':
        if human_is_left:
            answer = goal + r
        else:
            answer = r - goal
    elif operator == '/':  # division
        if human_is_left:
            answer = goal * r
        else:
            answer = r / goal
    else:
        assert False
    return int(answer)


def getAnswer(node, leaves, nodes, search_term, goal):
    # right or left must match search term
    if node["left"] == search_term:
        human_is_left = True
        ref = node["right"]
    elif node["right"] == search_term:
        human_is_left = False
        ref = node["left"]
    else:
        assert False

    if ref in leaves:
        r = leaves[ref]["value"]
    else:
        r = collect(nodes[ref], leaves, nodes)

    # update goal
    operator = node["op"]
    return reverseCalc(operator, goal, r, human_is_left)


def divideConquer(node, leaves, nodes, search_term, goal):
    assert node["op"]

    l = node["left"]
    r = node["right"]

    if l == search_term or r == search_term:
        return getAnswer(node, leaves, nodes, search_term, goal)

    if l in leaves:
        # human is in right branch
        ref_value = leaves[l]["value"]
        working_branch = nodes[r]  # assume it's a node
        human_is_left = False
    elif r in leaves:
        # human is in left branch
        ref_value = leaves[r]["value"]
        working_branch = nodes[l]  # assume it's a node
        human_is_left = True
    elif findMonkey(nodes[l], leaves, nodes, search_term):
        # human is in left branch
        ref_value = collect(nodes[r], leaves, nodes)
        working_branch = nodes[l]  # assume it's a node
        human_is_left = True
    else:
        # human is in right branch
        ref_value = collect(nodes[l], leaves, nodes)
        working_branch = nodes[r]  # assume it's a node
        human_is_left = False

    # update goal
    goal = reverseCalc(
        operator=node["op"], goal=goal, r=ref_value, human_is_left=human_is_left)

    return divideConquer(node=working_branch, leaves=leaves,
                         nodes=nodes, search_term=search_term, goal=goal)


def findMonkey(root, leaves, nodes, search_term):
    # return node that contains search_term in L or R
    if not root["op"]:
        return None  # it's a leaf, so no monkey

    left_name = root["left"]
    right_name = root["right"]

    if left_name == search_term or right_name == search_term:
        return root

    result = False
    if left_name in nodes:
        result = findMonkey(
            nodes[left_name], leaves, nodes, search_term)

    if not result and right_name in nodes:
        result = findMonkey(
            nodes[right_name], leaves, nodes, search_term)

    return result


def collect(root, leaves, nodes):
    if root["value"] != None:
        return root["value"]

    left_name = root["left"]
    if not isinstance(left_name, int):
        if left_name in leaves:
            root["left"] = leaves[left_name]["value"]
        else:
            root["left"] = collect(nodes[left_name], leaves, nodes)

    right_name = root["right"]
    if not isinstance(right_name, int):
        if right_name in leaves:
            root["right"] = leaves[right_name]["value"]
        else:
            root["right"] = collect(nodes[right_name], leaves, nodes)

    a = root["left"]
    b = root["right"]
    c = str("a" + root["op"] + "b")

    return int(eval(c))


def solve(lines, part):
    leaves = {}
    nodes = {}

    for line in lines:
        (monkey, s) = line.split(":")
        instruction = s.strip().split(" ")
        if len(instruction) == 1:
            leaves[monkey] = {"value": int(
                instruction[0]), "op": None, "left": None, "right": None}
        elif len(instruction) == 3:
            nodes[monkey] = {"value": None, "left": instruction[0],
                             "op": instruction[1], "right": instruction[2]}
        else:
            assert False

    if part == 1:
        result = collect(nodes["root"], leaves, nodes)
    else:  # part 2
        l = nodes["root"]["left"]
        r = nodes["root"]["right"]
        left_branch = nodes[l]
        right_branch = nodes[r]

        search_term = "humn"
        if findMonkey(
                left_branch, leaves, nodes, search_term):
            working_branch = left_branch
            reference_branch = right_branch
        elif findMonkey(
                right_branch, leaves, nodes, search_term):
            working_branch = right_branch
            reference_branch = left_branch
        else:
            assert False

        # Note that collect() modifies the tree
        goal = collect(reference_branch, leaves, nodes)

        result = divideConquer(node=working_branch, leaves=leaves,
                               nodes=nodes, search_term=search_term, goal=goal)

    return result


def main():
    filename = "input/d21.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines, part=1))
    print("Part 2:", solve(lines=lines, part=2))


if __name__ == '__main__':
    main()
