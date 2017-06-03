a = input()
n = len(a) + 1
b = input()
m = len(b) + 1

MAX = 999999

d = [MAX] * n
for i in range(n):
    d[i] = [MAX] * m


def editing_distance(i, j):
    if d[i][j] == MAX:
        if i == 0:
            d[i][j] = j
        elif j == 0:
            d[i][j] = i
        else:
            ins = editing_distance(i, j - 1) + 1
            del_ = editing_distance(i - 1, j) + 1
            sub = editing_distance(i - 1, j - 1) + (0 if a[i - 1] == b[j - 1] else 1)
            d[i][j] = min(ins, del_, sub)
    return d[i][j]

print(editing_distance(n - 1, m - 1))
