def updateFaces(farm, name, match_list):
    top = 0
    right = 1
    bottom = 2
    left = 3
    front = 4
    back = 5
    # default = [False, False, False, False, False, False]

    (x0, y0, z0) = map(int, name.split(","))

    for target in match_list:
        (x1, y1, z1) = map(int, target.split(","))

        zero = farm[name]
        one = farm[target]

        if x0 == x1:
            if y0 == y1:
                if z0 < z1:
                    zero[front] = one[back] = True
                else:
                    zero[back] = one[front] = True
            elif z0 == z1:
                if y0 < y1:
                    zero[top] = one[bottom] = True
                else:
                    zero[bottom] = one[top] = True
        elif y0 == y1:
            if z0 == z1:
                if x0 < x1:
                    zero[right] = one[left] = True
                else:
                    zero[left] = one[right] = True
        else:
            print("Error: Bad cube in target list")
    return farm


def matchTwo(names, target):
    match_list = []
    for name in names:
        name_a = name.split(",")
        target_a = target.split(",")
        sum = 0
        for i in range(len(target_a)):
            sum += abs(int(target_a[i]) - int(name_a[i]))
        assert sum != 0
        if sum == 1:
            match_list.append(name)
    return match_list


def solve(lines):
    farm = {}
    names = []  # just cube names, for simplicity

    for name in lines:
        match_list = matchTwo(names, name)

        farm[name] = [False, False, False, False, False, False]
        names.append(name)  # do this after matchTwo()

        farm = updateFaces(farm, name, match_list)

    result = 0
    for _, v in farm.items():
        for x in v:
            if not x:
                result += 1

    return result


def main():
    filename = "input/d18-pre"
    filename = "input/d18.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines))


if __name__ == '__main__':
    main()
