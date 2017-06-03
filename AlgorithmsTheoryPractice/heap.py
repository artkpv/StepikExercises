
from math import floor


# see BST in ..\exam_04dec2016\ex1.3.5_bst.py

# see

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
            if j + 1 < N and self._less(j, j + 1): j += 1
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


class MinHeap:
    def __init__(self):
        self._a = []

    def _validate(self, i):
        assert(0 <= i and i < len(self._a))

    def _swap(self, i, j):
        t = self._a[i]
        self._a[i] = self._a[j]
        self._a[j] = t

    def _swiftup(self, i):
        self._validate(i)
        parent = floor(i/2)
        self._validate(parent)
        if self._a[parent].compareto(self._a[i]) > 0:
            self._swap(parent, i)
            self._swiftup(parent)

    def _swiftdown(self, i):
        self._validate(i)
        first = min(len(self._a) - 1, i*2 + 1)
        second = min(len(self._a) - 1, i*2 + 2)
        self._validate(first)
        self._validate(second)
        max_ = first \
            if self._a[first].compareto(self._a[second]) > 0 \
            else second

        if self._a[max_].compareto(self._a[i]) > 0:
            self._swap(max_, i)
            self._swiftdown(max_)

    def insert(self, m):
        assert(type(m) is Node)
        self._a += [m]
        self._swiftup(len(self._a) - 1)

    def extractmin(self):
        if len(self._a) == 0:
            return None
        max_ = self._a[0]
        self._a[0] = self._a[len(self._a) - 1]
        del self._a[len(self._a) - 1]
        self._swiftdown(0)
        return max_

    def __str__(self):
        return str(self._a)
