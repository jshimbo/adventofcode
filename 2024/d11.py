def blink(stones, blinks):
    for _ in range(blinks):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                s = str(stones[i])
                half = len(s) // 2
                stones[i] = int(s[half:])
                stones.insert(i, int(s[:half]))
                i += 1
            else:
                stones[i] *= 2024
            i += 1

    return stones


def solve(lines):
    stones = [int(s) for s in lines[0].strip().split()]

    blinks_per_round = 5
    rounds = 5
    memo = {}

    for _ in range(rounds):
        hits = 0
        newlist = []
        for s in stones:
            if s in memo:
                hits += 1
                newlist.extend(memo[s])
            else:
                res = blink([s], blinks_per_round)
                newlist.extend(res)
                if not s in memo:
                    memo[s] = res

        stones = newlist

    return len(stones)


def main():
    input_file = "input/d11.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines))


if __name__ == "__main__":
    main()
