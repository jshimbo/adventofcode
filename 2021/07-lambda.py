# https://twitter.com/_alelouis/status/1468137246343585792


def solve(line, f):
    line_range = range(min(line), max(line)+1)
    return min([sum([f(n-t) for n in line]) for t in line_range])


input_file = "07-input"
lines = list(map(int, open(input_file).readline().split(',')))

print("part 1 answer:", solve(lines, lambda x: abs(x)))
print("part 2 answer:", solve(lines, lambda x: abs(x)*(abs(x)+1)/2))
