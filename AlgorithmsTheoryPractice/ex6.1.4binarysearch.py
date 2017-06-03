# https://stepik.org/lesson/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-13246/step/4?course=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B-%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0-%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B&unit=3431

first = input().split(' ')
n = int(first[0])
A = list(map(int, first[1:]))
assert(len(A) == n)
second = input().split(' ')
k = int(second[0])
B = list(map(int, second[1:]))
assert(len(B) == k)


def binarysearch(A, b):
    l = 0
    r = n - 1
    while l <= r:
        m = l + (r - l)//2
        if A[m] == b:
            return m
        elif A[m] > b:
            r = m -1
        else:
            l = m + 1
    return -1

import sys
for b in B:
    res = binarysearch(A, b)
    sys.stdout.write(str(res + 1 if res != -1 else res) + ' ')
