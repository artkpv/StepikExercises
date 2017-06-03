n = int(input())
a = list(map(int, input().split(' ')))
d = [-1] * (n + 2)
d[0] = 0
d[1] = 0


def ladder_sum_td(i):
    if d[i] == -1:
        d[i] = max(ladder_sum_td(i-1) + a[i - 2], ladder_sum_td(i-2) + a[i - 2])
    return d[i]

ladder_sum_td(n + 1)
print(d[n+1])
