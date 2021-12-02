def main():
    loc_x = 0
    depth = 0
    aim = 0
    with open("02-input") as fp:
        for line in fp:
            i = line.split()
            cmd = i[0]
            amount = int(i[1])
            if cmd == "forward":
                loc_x += amount
                depth += (amount * aim)
            elif cmd == "down":
                aim += amount
            elif cmd == "up":
                aim -= amount
            else:
                print("error")

    answer = depth * loc_x
    print(answer)


if __name__ == '__main__':
    main()
