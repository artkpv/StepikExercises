"""
Next:
    - Failed test #12. Wrong answer
      Check edge rules
"""

class Database:
    def __init__(self, tables, _max):
        self.tables = tables
        self.parents = list(range(len(tables)))
        self._max = _max

    def union(self, destination, source):
        if destination == source:
            return
        psource = self._find(source)
        pdestination = self._find(destination)
        if psource == pdestination:
            return
        self._move(pdestination, psource)
        if self._max < self.tables[pdestination]:
            self._max = self.tables[pdestination]

    def _move(self, destination, source):
        self.tables[destination] += self.tables[source]
        self.tables[source] = 0
        self.parents[source] = destination

    def _find(self, i):
        #while i != self.parents[i]:
        #    i = self.parents[i]
        if i != self.parents[i]:
            self._move(self.parents[i], i)
            self.parents[i] = self._find(self.parents[i])
        return self.parents[i]

    def max(self):
        return self._max

    def __repr__(self):
        return ' tables=' + str(self.tables) + ' parents=' + str(self.parents)

def readinput():
    n, m = [int(i) for i in input().strip().split(' ')]
    tables = []
    max_ = 0
    for raw in input().strip().split(' '):
        i = int(raw)
        if max_ < i:
            max_ = i
        tables += [i]
    assert(len(tables) == n)
    db = Database(tables, max_)
    # print(db)

    for i in range(m):
        dest, source = [int(i) for i in input().strip().split(' ')]
        db.union(dest - 1, source - 1)
        print(db.max())
        # print(db)

# ===============================================================

def test():
    from test import Tester
    t = Tester(__file__)

    t.test(
'''5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
''',
'''2
2
3
5
5''')

    t.test(
'''6 4
10 0 5 0 3 3
6 6
6 5
5 4
4 3''',
'''10
10
10
11''')

    t.test(
'''
6 4
0 0 0 0 0 0
6 6
6 5
5 4
4 3
''',
'''
0
0
0
0
''')

    t.test(
'''
6 4
0 0 0 0 0 1
6 6
6 5
5 4
4 3
''',
'''
1
1
1
1
''')

# MAX:
    t.test(
str.format('''
10000 9999
{}
{}
''',
           ' '.join([str(10000) for i in range(10000)]),
           '\n'.join([str(i) + ' ' + str(i + 1) for i in range(10000 - 1)])),
'\n'.join([str((i+2)*10000) for i in range(10000 - 1) ]))

# MIN:
    t.test(
'''
1 1
0
1 1
''',"0")


if __name__ == '__main__':
    import sys
    if '-t' in sys.argv:
        test()
    else:
        readinput()

