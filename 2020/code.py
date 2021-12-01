def check_triple(lines, anchor, target):
    print(".")
    lowwater = anchor + 1
    highwater = len(lines) - 1
    j = highwater

    while lowwater < j:
        sum = lines[anchor] + lines[lowwater] + lines[j]
        if sum == target:
            # print(f"anchor= {anchor} j= {lowwater} k={j}")
            return(lines[anchor] * lines[lowwater] * lines[j])
        elif lowwater == (j-1) or sum < target:
            lowwater += 1
            j = highwater
        elif sum > target:
            j -= 1
    # print(f"highwater= {j}, lowwater= {lowwater}")
    # print(f"anchor= {anchor}")
    return(0)


def get_answer(lines):
    # print(lines)
    anchor = 0
    highwater = len(lines) - 1

    while anchor < (highwater - 1):
        answer = check_triple(lines, anchor, 2020)
        if answer != 0:
            return(answer)
        else:
            anchor += 1

    # print(f"highwater= {j}, lowwater= {lowwater}, anchor= {anchor}")
    return(0)


def main():
    lines = []
    with open("01-input-sorted") as fp:
        for line in fp:
            lines.append(int(line))

    answer = get_answer(lines)
    if answer > 0:
        print(answer)
    else:
        print("No answer")


if __name__ == '__main__':
    main()
