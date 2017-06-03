#! python3
import sys


# Кол-во отрезков в которых точка:
#   все отрезки - отрезки заканчивающиеся до - открезки начинающиеся после

class Point:
    def __init__(self, x):
        self.x = x
        self.starts_after = 0
        self.ends_before = 0

START = 1
END = 2

n, m = map(int, input().split(' '))
intervals = []
for i in range(n):
    a, b = map(int, input().split(' '))
    intervals += [(a, b)]

in_points = list(Point(int(p)) for p in input().split(' '))

points = []
for p in in_points:
    points += [(p.x, p)]

for i in intervals:
    points.insert(0, (i[0], START))
    points.append((i[1], END))

points.sort(key=lambda x: x[0])

# move from both sides and count starts and ends:
starts = 0
ends = 0
for i in range(len(points)):
    # left side:
    left = points[i][1]
    if left == END:
        ends += 1
    elif type(left) is Point:
        left.ends_before = ends

    # right side:
    right = points[len(points) - i - 1][1]
    if right == START:
        starts += 1
    elif type(right) is Point:
        right.starts_after = starts

# point intertesections: all - intervals ends before - intervals starts after:
for i in in_points:
    sys.stdout.write(str(n - i.ends_before - i.starts_after) + ' ')
