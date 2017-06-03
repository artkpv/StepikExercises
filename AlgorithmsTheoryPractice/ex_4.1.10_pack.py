# python3
# Stepik - Algorithms - Ex. 4.1.10

n, W = map(int, input().split())

goods = []
for i in range(n):
    c, v = map(int, input().split())
    ratio = c * 1.0 / v
    goods += [(c, v, ratio)]

goods.sort(key=lambda x: x[2], reverse=True)

cost = 0.0
volume = 0.0
for g in goods:
    v = g[1]
    left = W - volume
    if left < v:
        volume += left
        cost += g[0] * (left/v)
        break
    else:
        volume += v
        cost += g[0]

print(cost)
