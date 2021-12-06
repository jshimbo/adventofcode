def census(pop):
    result = 0
    for x in pop:
        result += x
    return result


def main():
    input_file = "06-input"

    school = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # zero through eight

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line:
                s = line.split(',')
                for item in s:
                    i = int(item)
                    school[i] += 1

    num_days = 256

    print("Initial population is", census(school))
    print("After", num_days, "days")

    school_size = len(school)
    if (school_size != 9):
        print("ERROR: wrong school_size")
        return

    for day in range(num_days):
        for i in range(school_size):
            # shift left
            if i == 0:
                tmp = school[i]
            else:
                school[i-1] = school[i]
        school[8] = tmp
        school[6] += tmp
        # print(school)

    print("Number of lanternfish is", census(school))


if __name__ == '__main__':
    main()
