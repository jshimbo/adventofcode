def main():
    input_file = "06-input"
    num_days = 80
    school = []

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line:
                s = line.split(',')
                for i in range(len(s)):
                    school.append(int(s[i]))

    print("Initial number of fish ", len(school))
    print("Number of days ", num_days)

    while num_days > 0:
        num_days -= 1
        school_range = range(len(school))
        for i in school_range:
            if school[i] == 0:
                school[i] = 6
                school.append(8)
            else:
                school[i] -= 1

        # print(school)

    print("Number of fish ", len(school))


if __name__ == '__main__':
    main()
