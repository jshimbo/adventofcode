import sys

"""
Changes to my original solution
* Remove best guess trial run due to complexity
* Unify parts 1 and 2 by using lambdas, per
  per https://twitter.com/_alelouis/status/1468137246343585792
"""


def solve(crabs, f):
    locations = crabs.keys()
    line_range = range(min(locations), max(locations)+1)
    min_fuel = sys.maxsize

    for n in line_range:
        fuel = 0
        for k, v in crabs.items():
            fuel += f(n - k) * v
            if fuel > min_fuel:
                # Stop calculation since it's futile
                # Can reduce execution time by 40%
                break

        if min_fuel > fuel:
            min_fuel = fuel

    return min_fuel


def main():
    input_file = "07-input"

    crabs = {}
    lines = list(map(int, open(input_file).readline().split(',')))
    for i in lines:
        crabs[i] = crabs.get(i, 0) + 1

    # locations = crabs.keys()
    # print(len(lines), "crabs in", len(locations), "locations")
    # print("Lowest position", min(locations))
    # print("Highest position", max(locations))

    print("part 1 answer:", solve(crabs, lambda x: abs(x)))
    print("part 2 answer:", solve(crabs, lambda x: abs(x)*(abs(x)+1)/2))
    return


if __name__ == '__main__':
    main()
