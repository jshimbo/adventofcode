
def get_answer(lines):
    print(lines)
    lowwater = 0
    highwater = len(lines) - 1
    j = highwater
    # print(f"highwater= {highwater}, lowwater= {lowwater}")

    while lowwater < j:
        sum = lines[lowwater] + lines[j]
        if sum == 2020:
            return(lines[lowwater] * lines[j])
        elif lowwater == (j-1) or sum < 2000:
            lowwater += 1
            j = highwater
        elif sum > 2000:
            j -= 1
    print(f"highwater= {j}, lowwater= {lowwater}")
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
