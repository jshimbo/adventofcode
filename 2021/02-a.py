def main():
    loc_x = 0
    loc_y = 0
    with open("02-input") as fp:
        for line in fp:
            i = line.split()
            cmd = i[0]
            amount = int(i[1])
            if cmd == "forward":
                loc_x += amount
            elif cmd == "down":
                loc_y += amount
            elif cmd == "up":
                loc_y -= amount
            else:
                print("error")

    answer = loc_y * loc_x
    print(answer)


if __name__ == '__main__':
    main()
