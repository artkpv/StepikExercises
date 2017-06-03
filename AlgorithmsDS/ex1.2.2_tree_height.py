import sys
sys.setrecursionlimit(50000)

n = int(input())
parents = [int(i) for i in input().strip().split(' ')]
assert(n == len(parents))

children = [[] for i in range(n)]

root = None
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        children[parents[i]] += [i]

def get_height(v, height):
    max_ = height
    for c in children[v]:
        h = get_height(c, height) + 1
        if max_ < h:
            max_ = h
    return max_

print(get_height(root, 1))
