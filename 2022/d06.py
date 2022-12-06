def isUnique(chars):
    s = ""
    for c in chars:
        if c in s:
            return False
        s += c
    return True


def solve(data, marker_length):
    pos = 0
    chars = ""

    for c in data:
        chars += c
        pos += 1

        if len(chars) == marker_length:
            if isUnique(chars):
                return pos
            chars = chars[1:]

    return None


def main():
    input_file = "input/d06"
    with open(input_file) as f:
        line = f.read()

    print("Answer to part 1:", solve(line, 4))
    print("Answer to part 2:", solve(line, 14))


if __name__ == '__main__':
    main()
