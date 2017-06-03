# python3

# https://stepik.org/lesson/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0-%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC-13248/step/5?course=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B-%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0-%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B&unit=3433

"""
7 2 5 3 7 13 1 6

7 : 5
2 : 1
5 : 2
3 : 1
7 : 2
13 : 2
1 : 0
6 : 0
--
13
"""


swaps = 0
def merge(left, right):
    # print('merge(', left, ', ', right, ')')
    global swaps
    k, i, j = 0, 0, 0
    n = len(left) + len(right)
    new = [None] * n
    while k < n:
        if j == len(right):
            new[k] = left[i]
            i += 1
        elif i == len(left):
            new[k] = right[j]
            j += 1
        elif left[i] > right[j]:
            # print('SWAP', i, j, left, right)
            swaps += len(left) - i
            new[k] = right[j]
            j += 1
        elif left[i] <= right[j]:
            new[k] = left[i]
            i += 1
        k += 1
    return new


def mergesort(a, l=0, r=None):
    if r is None:
        r = len(a) - 1
    if l == r:
        return [a[l]]
    m = (r + l)//2
    return merge(mergesort(a, l, m), mergesort(a, m + 1, r))


def mergesort_iter(a):
    swaps = 0
    queue = []
    for i in a:
        queue += [[i]]

    if len(queue) % 2 != 0:
        queue += [[]]

    while len(queue) > 1:
        print(queue)
        left = queue.pop(0)
        right = queue.pop(0)
        assert(type(left) is list)
        assert(type(right) is list)

        k, i, j = 0, 0, 0
        n = len(left) + len(right)
        new = [None] * n
        while k < n:
            if j == len(right):
                new[k] = left[i]
                i += 1
            elif i == len(left):
                new[k] = right[j]
                j += 1
            elif left[i] > right[j]:
                print('SWAP', i, j, left, right)
                swaps += 1
                new[k] = right[j]
                j += 1
            elif left[i] <= right[j]:
                new[k] = left[i]
                i += 1
            k += 1

        queue += [new]

    print(queue)
    return swaps

n = int(input())
a = list(map(int, input().split(' ')))
# print(mergesort(a))
mergesort(a)
print(swaps)

#   YEAAAAAAHHHHHHHHHHHH! ДДДДДДДДАААААААААААААААААААААААААААААААААААААА!
