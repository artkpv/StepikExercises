# python3

n = int(input())
a = list(map(int, input().split()))
assert(len(a) == n)

if n == 0:
    print('0')
    exit()

b = [1] * n
for i in range(n):
    for j in range(i - 1, -1, -1):
        if a[i] % a[j] == 0 and b[j] + 1 > b[i]:
            b[i] = b[j] + 1

print(max(b))
