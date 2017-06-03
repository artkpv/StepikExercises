import sys
sys.setrecursionlimit(50000)

class DisjointSet:
    def __init__(self, n):
        self.a = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def union(self, l, r):
        lp = self.find(l)
        rp = self.find(r)
        if self.rank[lp] > self.rank[rp]:
            self.a[rp] = lp
        else:
            self.a[lp] = rp
            self.rank[lp] += 1

    def find(self, i):
        p = i
        while True: 
            if p == self.a[p]:
                break
            p = self.a[p]

        # flatten:
        # if i != self.a[i]:
        #    self.a[i] = self.find(self.a[i])
        return self.a[p]


def readinput():
    n, e, d = [int(i) for i in input().strip().split(' ')]
    ds = DisjointSet(n)
    for k in range(e):
        i, j = [int(i) for i in input().strip().split(' ')]
        i -= 1
        j -= 1
        ds.union(i, j)
    for k in range(d):
        i, j = [int(i) for i in input().strip().split(' ')]
        i -= 1
        j -= 1
        if ds.find(i) == ds.find(j):
            print(0)
            exit()
    print(1)

# ===============================================================

def test():
    from test import Tester
    t = Tester(__file__)

    t.test(
'''4 6 0
1 2
1 3
1 4
2 3
2 4
3 4''',
"1")

    t.test(
'''6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5''',
"0")

    t.test(
str.format('''100000 100000 100000
{}
{}''',
           '\n'.join(
               [str(i+1) + ' ' + str(i+2) for i in range(99999)]
               + ['1 1']
           ),
           '\n'.join(
               ['1 100000' for i in range(100000)]
           )
           ),
"1")



if __name__ == '__main__':
    import sys
    if '-t' in sys.argv:
        test()
    else:
        readinput()

