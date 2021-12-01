def main():
    count = 0
    prev_depth = False
    window = []
    with open("01-input") as fp:
        for line in fp:
            window.append(int(line))
            if len(window) > 3:
                window.pop(0)
                depth = window[0] + window[1] + window[2]
                if depth > prev_depth:
                    count += 1
                prev_depth = depth
            elif len(window) == 3:
                prev_depth = window[0] + window[1] + window[2]

    print(count)


if __name__ == '__main__':
    main()
