"""
https://stepik.org/lesson/Задачи-41562/step/2?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=20016

NEXT:
    - optimize: Failed test #26. Time limit exceeded
"""
import logging as log
from logging import debug
log.basicConfig(level=log.INFO, format='%(message)s')

class Node:
    def __init__(self, next_, value):
        self.next = next_
        self.value = value

class MyDict:
    def __init__(self, m):
        self.a = [None for i in range(m)]

    def __repr__(self):
        s = ''
        for i in range(len(self.a)):
            a = None
            if i is not None:
                a = self.check(i)
            s += str(i) + ': ' + (a if a is not None else '[None]') + '\n'
        return s

    def _hash(self, v):
        x = 263
        p = 1000000007
        if v is None:
            return None
        sum_ = 0
        for i in range(len(v)):
            sum_ += (ord(v[i])*(x**i))
            sum_ %= p

        h = sum_%len(self.a)
        return h

    def add(self, v):
        h = self._hash(v)
        if self.a[h] == None:
            self.a[h] = Node(None, v)
        else:
            doesExist = self.find(v, h)
            if not doesExist:
                first = self.a[h]
                n = Node(first, v)
                self.a[h] = n

    def check(self, i):
        node = self.a[i]
        s = ''
        while node != None:
            s += node.value + ' '
            node = node.next
        return s

    def find(self, v, hp = None):
        h = hp if hp != None else self._hash(v)
        node = self.a[h]
        while node != None:
            if node.value == v:
                return True
            node = node.next
        return False

    def delete(self, v):
        h = self._hash(v)
        prev = None
        node = self.a[h]
        while node != None:
            if node.value == v:  # remove node:
                if prev != None:
                    prev.next = node.next
                else:  # it is first one
                    self.a[h] = node.next
                return

            prev = node
            node = node.next

def main():
    m = int(input().strip())
    n = int(input().strip())

    d = MyDict(m)
    for i in range(n):
        c = input().strip().split(' ')
        a = c[0]
        if a == 'add':
            d.add(c[1])
        elif a == 'check':
            print(d.check(int(c[1])))
        elif a == 'find':
            found = d.find(c[1])
            print('yes' if found else 'no')
        elif a == 'del':
            d.delete(c[1])

        debug(str(d))

def test():
    d = MyDict(5)
    h = d._hash('world')
    assert(h == 4)
    print('Hash for "world" =', h)


    from test import Tester
    t = Tester(__file__)
    t.test('''5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good''',
           '''HellO world
no
yes
HellO
GooD luck''')


if __name__ == '__main__':
    import sys
    if '-t' in sys.argv:
        test()
    else:
        main()

