
W, N = map(int, input().split(' '))
weights = list(map(int, input().split(' ')))
assert(len(weights) == N)
d = [0] * (N + 1)  # cost of knapsack with i gold blocks; 0 - no blocks
for i in range(N + 1):
    d[i] = [0] * (W + 1)  # 0 - no space in knapsack

COST = 1

for w in range(1, W + 1):
    for i in range(1, N + 1):
        wi = weights[i - 1]
        d[i][w] = d[i - 1][w]  # was taken already
        if wi <= w:  # i-th gold block can be taken in this knapsack
            d[i][w] = max(
                d[i][w],  # without this block
                d[i - 1][w - wi] + COST * wi)  # with this block

"""
import sys
print('   ' + ' '.join(str(j) for j in range(len(d[0]))))
for i in range(len(d)):
    sys.stdout.write(str(i) + ': ')
    print(' '.join(str(j) for j in d[i]))
"""

print(d[N][W])
