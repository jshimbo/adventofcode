import enum
from os import getenv
import sys
from unittest.case import skip

input_file = "input/18-input-test"


def addition(x, y):
    if not x:
        return y

    newlist = ['[']
    for i in x:
        newlist.append(i)
    for i in y:
        newlist.append(i)
    newlist.append(']')
    return newlist


def split10s(tokens):
    newlist = []
    done = False
    for ptr, t in enumerate(tokens):
        if not done and isinstance(t, int) and t > 9:
            t = t/2
            x = int(t)
            y = int(t + 0.5)
            res = ['[', x, y, ']']
            for x in res:
                newlist.append(x)
            done = True
        else:
            newlist.append(t)
    return newlist


def explode(tokens):
    level = 0
    newlist = []
    uxo = 0
    exploded = False  # one explosion per round
    skip_one = False

    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF")

    for _, t in enumerate(tokens):
        if t == '[':
            level += 1
            newlist.append(t)
        elif t == ']':
            level -= 1
            if skip_one:
                # because we exploded
                skip_one = False
            else:
                newlist.append(t)
        elif isinstance(t, int):
            # Token is a number
            if uxo:
                # add R-val to first number to the right
                newlist.append(t + uxo)
                uxo = 0
            elif exploded or level < 5:
                # Done or not nested enough to explode
                newlist.append(t)
            elif not isinstance(newlist[-1], int):
                # possible singleton or not yet a pair
                newlist.append(t)
            else:
                # we found a pair

                # First deal with the r-value
                uxo = t  # unexploded ordinance

                # get first number in pair
                first = newlist.pop()

                # Add to closest number to left
                # newlist[0] and newlist[-1] should be '['
                for i in range(len(newlist)-2, 0, -1):
                    if isinstance(newlist[i], int):
                        newlist[i] += first
                        break

                # Replace pair with zero
                check = newlist[-1]  # '['
                if check != '[':
                    print("Assert failed. Expected [. Got", check)
                    sys.exit()
                # Remove previously saved '['
                newlist[-1] = 0
                skip_one = True  # skip next ']'
                exploded = True  # done for this round

    return newlist


def tokenize(chars):
    """Convert a string of characters into a list of tokens."""
    # Idea from http://norvig.com/lispy.html
    line = chars.replace(
        '[', ' [ ').replace(']', ' ] ').replace(',', ' ').split()

    for i, v in enumerate(line):
        if v != '[' and v != ']':
            line[i] = int(v)
    return(line)


# end parsing code

def magnitude(line):
    newline = []
    skip_next = False

    if len(line) == 1:
        # print("Found answer. End recursion.")
        return line

    # Process pairs, then recurse.
    # Eventually return a list with one element
    for c in line:
        if skip_next:
            skip_next = False
        elif c == '[':
            newline.append(c)
        elif c == ']':
            newline.append(c)
        elif isinstance(c, int):
            if isinstance(newline[-1], int):
                # found a pair
                # get Lval
                lval = newline.pop()
                x = lval * 3 + c * 2
                newline.pop()  # pop previous '['
                newline.append(x)
                skip_next = True  # skip next char, ']'
            else:
                newline.append(c)

    return magnitude(newline)


def print_list(label, list):
    """Print in original form to aid tests"""
    print(label, end='')
    prev = ""
    line = ""
    for c in list:
        # insert comma when needed
        if isinstance(prev, int) and c != ']':
            # after number, except before closing bracket
            line += ','
        elif prev == ']' and c == '[':
            # between two backets
            line += ','
        elif prev == ']' and isinstance(c, int):
            # between closing bracket and number
            line += ','
        if isinstance(c, int):
            line += str(c)
        else:
            line += c
        prev = c
    print(line)


def has_level_five(line):
    """Check if we need to explode"""
    count = 0
    for c in line:
        if c == '[':
            count += 1
            if count > 4:
                return True
        elif c == ']':
            count -= 1
    return False


def has_tens(list):
    """Check if need to split"""
    return any(isinstance(i, int) and i > 9 for i in list)


def reduce(line):
    go_again = True  # go at least once
    while go_again:
        go_again = False
        while has_level_five(line):
            line = explode(line)
            # print_list("After explode: ", line)

        if has_tens(line):
            line = split10s(line)
            # print_list("After split:   ", line)
            go_again = True

    return line


def mainloop(lines):
    prev = l = []
    one_liner = True if len(lines) == 1 else False

    for line in lines:
        # print("New line")
        # print(line)

        prev = l
        l = tokenize(line)

        if prev == []:
            # first line of input
            skip = True
        else:
            l = addition(prev, l)
            # print_list("After add:     ", l)
            skip = False

        if one_liner or not skip:
            l = reduce(l)

    return(l)


def main():
    with open(input_file if len(sys.argv) < 2 else sys.argv[1], encoding="utf-8") as fp:
        data = fp.read().splitlines()

    result = mainloop(data)
    # print("mainloop() returns", result)
    mag = magnitude(result)
    print("Part 1 magnitude is", mag[0])

    max_mag = 0
    for i, v1 in enumerate(data):
        for j, v2 in enumerate(data):
            if i != j:
                result = mainloop([v1, v2])
                mag = magnitude(result)
                if mag[0] > max_mag:
                    max_mag = mag[0]
    print("Part 1 maximum magnitude is", max_mag)


if __name__ == '__main__':
    main()
