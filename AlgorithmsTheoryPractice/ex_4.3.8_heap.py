# python3


class Node:
    def __init__(self, weight, val=None):
        assert(weight is not None)
        self.weight = weight
        self.val = val

    def compareto(self, other):
        assert(type(other) is Node)
        return self.weight - other.weight

    def __str__(self):
        return'<Node {} {}>'.format(
            self.weight, self.val if self.val else '')

    def __repr__(self):
        return str(self)


class MaxHeap:
    def __init__(self):
        self._a = []

    def _validate(self, i):
        assert(0 <= i and i < len(self._a))

    def _swap(self, i, j):
        t = self._a[i]
        self._a[i] = self._a[j]
        self._a[j] = t

    def _less(self, i, j):
        return self._a[i].compareto(self._a[j]) < 0

    def _swimup(self, i):
        while i > 0 and self._less(int(i/2), i):
            self._swap(int(i/2), i)
            i = int(i/2)

    def _sink(self, i):
        N = len(self._a)
        while 2*i < N:
            j = 2*i
            if j + 1 < N and self._less(j, j + 1):
                j += 1
            if not self._less(i, j):
                break
            self._swap(i, j)
            i = j

    def insert(self, m):
        assert(type(m) is Node)
        self._a += [m]
        self._swimup(len(self._a) - 1)
        pass

    def extractmax(self):
        if len(self._a) == 0:
            return None
        max_ = self._a[0]
        self._a[0] = self._a[len(self._a) - 1]
        del self._a[len(self._a) - 1]
        self._sink(0)
        return max_

    def __str__(self):
        return str(self._a)


heap = MaxHeap()
n = int(input())
for i in range(n):
    op = input().split(' ')
    if op[0] == 'Insert':
        heap.insert(Node(int(op[1])))
    elif op[0] == 'ExtractMax':
        print(heap.extractmax().weight or '')
