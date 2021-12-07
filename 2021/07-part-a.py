import sys


def calc_cost(crabs, target, cost_to_beat):
    cost = 0
    for guess in crabs:
        if guess != target:
            distance = abs(target - guess)
            cost += distance * crabs.get(guess)
        if cost > cost_to_beat:
            cost = False
            break

    return(cost)


def make_best_guess(crabs):
    sum = 0
    pop = 0
    for x in crabs:
        y = crabs.get(x)
        pop += y
        sum += x * y
    return(int(sum/pop))


def main():
    input_file = "07-input"

    crabs = {}
    population = 0
    lowest = 99999
    highest = 0

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line:
                s = line.split(',')
                for i in s:
                    i = int(i)
                    crabs[i] = crabs.get(i, 0) + 1
                    if i < lowest:
                        lowest = i
                    if i > highest:
                        highest = i
                    population += 1

    print("Population:", population)
    print("Lowest position", lowest)
    print("Highest position", highest)
    print("Locations", len(crabs))

    # calculate best guess
    best_guess = make_best_guess(crabs)
    cost_to_beat = calc_cost(crabs, best_guess, sys.maxsize)
    print("Cost to beat is", cost_to_beat, "for position", best_guess)

    for x in range(lowest, highest+1):
        cost = calc_cost(crabs, x, cost_to_beat)
        if cost and cost < cost_to_beat:
            print("Position", x, "Cost", cost)
            cost_to_beat = cost


if __name__ == '__main__':
    main()
