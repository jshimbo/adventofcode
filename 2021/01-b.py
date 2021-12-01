def main():
    count = 0
    index = 0
    prev_depth = False
    window = []
    with open("01-input") as fp:
        for line in fp:
            if index < 3:
                window.append(int(line))
                index += 1
                if index == 3:
                    prev_depth = window[0] + window[1] + window[2]
                continue
            else:
                window[0] = window[1]
                window[1] = window[2]
                window[2] = int(line)

            depth = window[0] + window[1] + window[2]

            if depth > prev_depth:
                count += 1
            prev_depth = depth

    print(count)


if __name__ == '__main__':
    main()
