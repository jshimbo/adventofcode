def collate(locks) -> dict:
    keyring = {}
    for lock in locks:
        total = sum(lock)
        keyring.setdefault(total, []).append(lock)

    return keyring


def it_fits(locks, keys) -> int:
    count = 0
    nope = False
    for lock in locks:
        for key in keys:
            nope = False
            for i in range(len(key)):
                if key[i] + lock[i] > 5:
                    nope = True
                    break
            if not nope:
                count += 1

    return count


def solve(lines):
    locks = []
    keys = []

    get_key = False
    get_lock = False
    row_index = 0
    tmp = [0] * 5

    for line in lines:
        line = line.strip()
        if not line:
            # empty line
            get_key = False
            get_lock = False
            row_index = 0
            tmp = [0] * 5
        elif get_key or get_lock:
            if row_index < 5:
                for i, c in enumerate(line):
                    if c == "#":
                        tmp[i] += 1
                row_index += 1
            else:
                if get_key:
                    keys.append(tmp.copy())
                    get_key = not get_key
                elif get_lock:
                    locks.append(tmp.copy())
                    get_lock = not get_lock
        else:
            # first line after a blank line
            if line == ".....":
                # Key
                get_key = True
                get_lock = not get_key
            elif line == "#####":
                # Lock
                get_key = False
                get_lock = not get_key

    # The last one
    if get_key:
        keys.append(tmp.copy())
    elif get_lock:
        locks.append(tmp.copy())

    locks = collate(locks)
    keys = collate(keys)

    combinations = 0
    for lock_sum, lock_list in locks.items():
        for key_sum, key_list in keys.items():
            if lock_sum + key_sum <= 25:
                combinations += it_fits(lock_list, key_list)

    print("Answer to part 1:", combinations)


def main():
    input_file = "input/d25.txt"

    with open(input_file) as f:
        lines = f.readlines()

    solve(lines)


if __name__ == "__main__":
    main()
