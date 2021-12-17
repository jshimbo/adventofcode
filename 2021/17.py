import sys

# test
target_area = [(20, -10), (30, -5)]

# Real target area: x=207..263, y=-115..-63
target_area = [(207, -115), (263, -63)]

x_min = min(target_area[0][0], target_area[1][0])
x_max = max(target_area[0][0], target_area[1][0])

y_max = max(target_area[0][1], target_area[1][1])
y_min = min(target_area[0][1], target_area[1][1])


def hit(x, y):
    if x > x_max or y < y_min:
        # overshoot
        res = -1
    elif x >= x_min and y <= y_max:
        # hit
        res = 1
    else:
        res = 0  # keep going
    return res


def shoot(dx, dy):
    x = y = 0
    apex = 0  # highest point of shot
    steps = 0  # in case of endless loop
    res = 0
    while res == 0:
        x += dx
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        y += dy
        dy -= 1

        if y > apex:
            apex = y

        res = hit(x, y)

        # Check for endless loop
        steps += 1
        if (steps > 10000):
            res = -2
    return res, apex


# shots = [(7, 2), (6, 3), (9, 0), (17, -4), (6, 9)]
shots = []
# dx can never exceed farthest point on target (x_max)
# negative dy can never exceed the lower point on target (y_min)
for dx in range(x_max + 1):
    for dy in range(y_min - 1, 150):
        shots.append((dx, dy))

# scores
highest_point = 0
num_hits = 0

# diagnostics
min_dx = 9999
max_dx = 0
min_dy = 9999
max_dy = 0


for shot in shots:
    dx, dy = shot

    winner, max_y = shoot(dx, dy)

    if winner == 1:
        # Hit. Score it.
        num_hits += 1
        if max_y > highest_point:
            highest_point = max_y
        # diagnostics
        # print(shot)
        if dx < min_dx:
            min_dx = dx
        if dx > max_dx:
            max_dx = dx
        if dy > max_dy:
            max_dy = dy
        if dy < min_dy:
            min_dy = dy
    elif winner == -1:
        # over shot, opportunity to optimize
        pass
    elif winner == -2:
        # Too many steps, likely error in code
        print("+", end="")
    else:
        print("ERROR Invalid return code")

print("Answers")
print("  The highest point", highest_point)
print("  Number of hits", num_hits)
print("---------------")
print("X min and max:", x_min, x_max)
print("Y min and max:", y_min, y_max)
print("---------------")
print("Min, max dx", min_dx, max_dx)
print("Min, Max dy", min_dy, max_dy)
