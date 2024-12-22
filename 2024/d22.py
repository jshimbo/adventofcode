def secret(s, rounds):
    secret = int(s.strip())
    secret_numbers = [secret]

    for _ in range(rounds):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        secret_numbers.append(secret)

    return secret_numbers


def priceList(buyers):
    price_list = {}
    for buyer_id, buyer in enumerate(buyers):
        for i in range(len(buyer) - 4):
            diffs = [buyer[j] % 10 - buyer[j - 1] % 10 for j in range(i + 1, i + 5)]
            value = buyer[i + 4] % 10

            h = "".join(map(str, diffs))  # hash list
            if h in price_list:
                if buyer_id not in price_list[h]["buyer_ids"]:
                    price_list[h]["value"] += value  # sum value for all buyers
                    price_list[h]["buyer_ids"].append(buyer_id)
            else:
                price_list[h] = {"value": value, "seq": diffs, "buyer_ids": [buyer_id]}

    return price_list


def solve(lines):
    rounds = 2000
    buyers = [secret(line, rounds) for line in lines]

    print("Part 1:", sum(b[-1] for b in buyers))

    price_list = priceList(buyers)
    max_item = max(price_list.values(), key=lambda v: v["value"])
    max_value = max_item["value"]
    sequence = max_item["seq"]

    print("Part 2:", max_value)
    # print("Sequence:", sequence)


def main():
    input_file = "input/d22.txt"

    with open(input_file) as f:
        lines = f.readlines()

    solve(lines)


if __name__ == "__main__":
    main()
