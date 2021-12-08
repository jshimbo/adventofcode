def get_message(s):
    """The message is to the right of vertical bar"""
    return(s.split('|')[1].strip())


def solve1(input):
    """Solve part 1"""
    bins = {}
    msgs = list(map(get_message, input))

    for msg in msgs:
        words = msg.split()
        for word in words:
            l = len(word)
            bins[l] = bins.get(l, 0) + 1
    return(bins[2] + bins[4] + bins[3] + bins[7])


def decode_msg(decoder, msg):
    clear_words = []
    words = msg.split()
    for word in words:
        s = "".join(sorted(word))  # alphbetize for lookup
        clear_words.append(decoder.get(s))
    result = "".join(clear_words)
    return result


def is_subset(hint, target):
    """Is subset"""
    h = set(hint)
    t = set(target)
    return h.issubset(t)


def match_three(hint, target):
    """Check if matching three out of four"""
    h = set(hint)
    t = set(target)
    return len(h.intersection(t)) == 3


def create_decoder(bins):
    decoder = {}

    # Find the unique digits
    for s in bins:
        slen = len(s)
        if slen == 2:
            decoder[1] = decoder.get(1, s)
        elif slen == 3:
            decoder[7] = decoder.get(7, s)
        elif slen == 4:
            decoder[4] = decoder.get(4, s)
        elif slen == 7:
            decoder[8] = decoder.get(8, s)

    # Suss out the remaining digits
    for s in bins:
        slen = len(s)
        if slen == 5:
            # 2, 3, or 5 have five segments
            if is_subset(decoder[1], s):
                # 3 should all pins of 1
                decoder[3] = decoder.get(3, s)
            elif match_three(decoder[4], s):
                # 5 should match three pins of 4
                decoder[5] = decoder.get(5, s)
            else:
                # 2 remains
                decoder[2] = decoder.get(2, s)

        elif slen == 6:
            # 0, 6, or 9 have six segments
            if is_subset(decoder[4], s):
                # 4 is a subset of 9
                decoder[9] = decoder.get(9, s)
            elif is_subset(decoder[7], s):
                # 7 is a subset of 0, but check the above first
                decoder[0] = decoder.get(0, s)
            else:
                # 6 remains
                decoder[6] = decoder.get(6, s)

    # swap key and value
    inv_map = {v: str(k) for k, v in decoder.items()}
    return inv_map


def create_keys(line):
    """Return list of unique words"""
    bins = {}
    for number in line.split():
        if number != '|':
            # sort digits in number
            s = "".join(sorted(number))
            bins[s] = bins.get(s, 0) + 1
    return(list(bins.keys()))


def solve2(lines):
    answer = 0
    for line in lines:
        keys = create_keys(line)
        decoder = create_decoder(keys)
        message = get_message(line)
        cleartext = decode_msg(decoder, message)
        answer += int(cleartext)

    return answer


def main():
    input_file = "08-input"
    lines = open(input_file).readlines()

    print("Answer 1", solve1(lines))
    print("Answer 2", solve2(lines))
    return


if __name__ == '__main__':
    main()
