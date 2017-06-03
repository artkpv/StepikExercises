# python3
import sys

"""
Небольшая подсказка для тех, кто не понимает, как подойти к решению или
уперся в своем решении в предел по времени. Попробуйте представить,
что у вас на прямой отмечены точки начал отрезков, концов отрезков и
контрольные точки. Если начать движение вдоль прямой начиная с самой
маленькой точки, подсчитывать количества начал и концов отрезков, то
для каждой контрольной точки не составит труда определить скольким отрезкам она принадлежит.
"""

class BST:
    class Node:
        def __init__(self, v, size, left=None, right=None):
            self.size = size
            self.value = v
            self.left = left
            self.right = right
            self.times = 1

        def __str__(self):
            return '<Node {} val, {} size, {} times'.format(
                    self.value, self.size, self.times)

    def __init__(self):
        self.root = None

    def size_all(self):
        return self.size(self.root)

    def size(self, node):
        if node is None:
            return 0
        return node.size

    def times(self, v):
        node = self._get(self.root, v)
        return node.times if node else 0

    def _get(self, node, v):
        if node is None:
            return None
        elif node.value == v:
            return node
        elif v < node.value:
            return self._get(node.left, v)
        else:  # node.value > v:
            return self._get(node.right, v)

    def put(self, v):
        self.root = self._put(self.root, v)

    def _put(self, x, v):
        if x is None:
            return BST.Node(v, 1)
        if v < x.value:
            x.left = self._put(x.left, v)
        elif x.value < v:
            x.right = self._put(x.right, v)
        else:
            x.value = v
            x.times += 1
        x.size = self.size(x.left) + self.size(x.right) + x.times
        return x

    def lt(self, v):
        return self._lt(self.root, v)

    def _lt(self, node, v):
        # print('_lt(', node, v, ')')
        if node is None:
            return 0
        if node.value == v:
            return self.size(node.left)
        elif v > node.value:
            return node.times + self.size(node.left) + self._lt(node.right, v)
        else:  # v < node.value
            return self._lt(node.left, v)

    def _tostring(self, node, lvl):
        if node is None:
            return ''
        s = '\n' + (' ' * lvl) + str(node)
        s += '\n' + (' ' * lvl) + ' left:'
        s += self._tostring(node.left, lvl + 1)
        s += '\n' + (' ' * lvl) + ' right:'
        s += self._tostring(node.right, lvl + 1)
        s += '>'
        return s

    def __str__(self):
        s = self._tostring(self.root, 0)
        return s


n, m = map(int, input().split(' '))
starts = BST()
ends = BST()
for i in range(n):
    a, b = map(int, input().split(' '))
    starts.put(a)
    ends.put(b)

# print("starts:")
# print(starts)
# print("ends:")
# print(ends)

for p in map(int, input().split(' ')):
    ends_lt = ends.lt(p)
    starts_gt = starts.size_all() - starts.lt(p) - starts.times(p)
    crosses = n - ends_lt - starts_gt
    # print('point=', p, ' starts_gt=', starts_gt, ' ends_lt=', ends_lt, 'croosses=', crosses)
    sys.stdout.write(str(crosses) + ' ')
