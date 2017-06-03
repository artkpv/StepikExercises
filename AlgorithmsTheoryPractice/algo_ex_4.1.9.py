# python3

"""

---
  -----
     ----
-
            -

"""

n = int(input())
intervals = []
for i in range(n):
    x1, x2 = map(int, input().split())
    intervals += [(x1, x2)]

intervals.sort(key=lambda x: x[1])

points = []
current = None
for i in intervals:
    if current and i[0] <= current[1]:
        continue
    current = i
    points += [i[1]]

print(len(points))
for p in points:
    print(p)
