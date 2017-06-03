n = int(input())
a = []
m = 10
for i in map(int, input().split(' ')):
    i = i - 1
    a += [i]
    assert(0 <= i and i < m)
assert(len(a) == n)

b = [0] * m

for i in range(n):
    b[a[i]] += 1

for i in range(1, m):
    b[i] = b[i] + b[i - 1]

a_sorted = [None] * n
for i in range(n - 1, -1, -1):
    a_sorted[b[a[i]] - 1] = a[i]
    b[a[i]] -= 1
print(' '.join(str(i + 1) for i in a_sorted))
