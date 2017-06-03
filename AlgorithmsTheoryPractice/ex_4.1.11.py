# python3

"""

n = 20
1 + 2 + 3 + 4 + 5 + 6
"""

n = int(input())

components = []
sum_ = 0
for c in range(1, n + 1):
    sum_ += c
    components += [c]
    if sum_ == n:
        break
    if sum_ > n:
        prev = components.pop()
        sum_ -= prev
        prev = components.pop()
        sum_ -= prev
        c = n - sum_
        sum_ += c
        components += [c]
        break

print(len(components))
print(' '.join(map(str, components)))
