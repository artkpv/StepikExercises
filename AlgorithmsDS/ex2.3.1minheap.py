"""
https://stepik.org/lesson/Задачи-41560/step/1?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=20013
"""
n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]

swaps = []
def doswap(i, j, a):
    global swaps
    swaps += [(i, j)]
    t = a[i]
    a[i] = a[j]
    a[j] = t

def sift_down(i, a):
    global swaps
    l = i*2+1
    r = i*2+2
    if r < len(a) and a[r] < a[l] and a[i] > a[r]:
        doswap(i, r, a)
        sift_down(r, a)
    if l < len(a) and a[l] < a[i]:
        doswap(i, l, a)
        sift_down(l, a)

for i in range(len(a) - 1, -1, -1):
    sift_down(i, a)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])


