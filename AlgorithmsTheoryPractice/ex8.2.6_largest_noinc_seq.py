# python3

# TODO: should work in O(n*log(n)) time
# fails at 8th test

n = int(input())
a = list(map(int, input().split()))
assert(len(a) == n)

if n == 0:
    print('0')
    exit()

prev = [-1] * n
b = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] >= a[i] and b[j] > b[i] - 1:
            b[i] = b[j] + 1
            prev[i] = j

max_ = max(b)
i = b.index(max_)
seq = [i]
while i > 0:
    j = prev[i]
    seq += [j]
    i = j

print(max_)
print(' '.join(str(i + 1) for i in reversed(seq)))
