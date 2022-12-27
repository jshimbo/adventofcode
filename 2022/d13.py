# Day 13: Distress Signal

from functools import cmp_to_key


def stringToList(message):
    parts = []
    level = 0
    i = 0
    msglen = len(message)
    while i < msglen:

        c = message[i]
        i += 1

        if c == ']':
            level -= 1
            if level > 0:
                s += c
            else:
                # discard and done
                done = True
        elif c == '[':
            level += 1
            if level == 2:  # discard initial '['
                # collect chars until and including matching bracket
                s2 = c
                done = False
                while level > 1:
                    assert i < msglen
                    c = message[i]
                    i += 1
                    s2 += c
                    if c == ']':
                        level -= 1
                    elif c == '[':
                        level += 1
                parts.append(s2)
        elif c.isdigit():
            # read digits until ',' or ']'
            s = c
            done = False
            while not done:
                assert i < msglen
                c = message[i]
                i += 1
                if c.isdigit():
                    s += c
                else:
                    parts.append(int(s))
                    s = ""
                    done = True
                    if c == ']':
                        i -= 1  # push back into input queue

    return parts


def compareLists(one, two):
    # Returns
    #  -1 : left < right
    #  +1 : left > right
    #   0 : a tie

    l_len = len(one)
    r_len = len(two)

    if l_len == 0 and r_len > 0:
        return -1

    if r_len == 0 and l_len > 0:
        return 1

    result = 0
    msglen = min([l_len, r_len])
    for i in range(msglen):
        if result != 0:
            break

        left = one[i]
        right = two[i]

        if isinstance(left, int):
            if isinstance(right, int):
                # https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons
                result = (left > right) - (left < right)
            else:
                left = [left]
                right = stringToList(right)
                result = compareLists(left, right)
        else:
            left = stringToList(left)
            if isinstance(right, int):
                right = [right]
            else:
                right = stringToList(right)
            result = compareLists(left, right)

    if result == 0:
        # tie breaker
        result = (l_len > r_len) - (l_len < r_len)

    return result


def compareMessages(message0, message1):
    # for Part 1
    one = stringToList(message0)
    two = stringToList(message1)

    result = compareLists(one, two)

    assert result != 0
    if result < 0:
        result = True
    elif result > 0:
        result = False

    return result


def solve(msg_pairs, part):
    if part == 1:
        result = 0
        message_number = 1
        for msg_pair in msg_pairs:
            pair = msg_pair.split("\n")
            if compareMessages(pair[0], pair[1]):
                result += message_number
            message_number += 1

    else:  # part 2
        array = []

        l = stringToList("[[2]]")
        array.append(l)

        for msg_pair in msg_pairs:
            pair = msg_pair.split("\n")
            # Do not loop on pair because of the last line
            l = stringToList(pair[0])
            array.append(l)
            l = stringToList(pair[1])
            array.append(l)

        l = stringToList("[[6]]")
        array.append(l)
        array = sorted(array, key=cmp_to_key(compareLists))

        marker1 = stringToList("[[2]]")
        marker2 = stringToList("[[6]]")
        i = 0
        x = y = 0
        for line in array:
            i += 1
            if line == marker1:
                x = i
            elif line == marker2:
                y = i
        result = x * y

    return result


def main():
    filename = "input/d13.txt"
    with open(filename) as f:
        pairs = f.read().split("\n\n")

    print("Part 1:", solve(msg_pairs=pairs, part=1))
    print("Part 2:", solve(msg_pairs=pairs, part=2))


if __name__ == '__main__':
    main()
