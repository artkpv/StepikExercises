#! python3

import sys
sys.setrecursionlimit(50000)

_dump = ""

"""
https://stepik.org/lesson/Задачи-45970/step/4?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=24123

NEXT
- Failed test #69. Time limit exceeded

"""

import logging as log
from logging import debug, info
import sys

if '-vv' in sys.argv:
    log.basicConfig(level=log.DEBUG, format='%(message)s')
elif '-v' in sys.argv:
    log.basicConfig(level=log.INFO, format='%(message)s')
else:
    log.basicConfig(level=log.WARN, format='%(message)s')

def inorder(v=None):
    if v == None:
        return []
    s = []
    if v.l != None:
        s += inorder(v.l)
    s += [v.key]
    if v.r != None:
        s += inorder(v.r)
    return s

def get_tree_string(v=None, level=0):
    if v == None:
        return "[empty]"
    s = ""
    if v.l != None:
        s += get_tree_string(v.l, level + 1)
    s += " " * level + "{:,}({:,})\n".format(v.key, v.sum)
    if v.r != None:
        s += get_tree_string(v.r, level + 1)
    return s


class Node:
    def __init__(self, key):
        self.p = None
        self.l = None
        self.r = None
        self.key = key
        self.sum = key

    def isLeaf(self):
        return self.l == None and self.r == None

    def refresh_sum(self, updateParents=True):
        #debug(' refresh_sum {}'.format(self.key))
        self.sum = self.key
        self.sum += self.l.sum if self.l != None else 0
        self.sum += self.r.sum if self.r != None else 0
        if updateParents and self.p != None:
            self.p.refresh_sum()


class BstOfSum:
    def __init__(self):
        self.lastsum = 0
        self.root = None
        self._split_common_child = None
        self.lastlen = 0

    #def _assert_invariants(self, t, expectedlen=None):
    #    tsum = t.sum if t else 0
    #    a = inorder(t) if t else []
    #    tlen = len(a)
    #    if expectedlen != None:
    #        assert expectedlen == tlen, "expected:{}, actual:{}".format(expectedlen, tlen)
    #    self.lastlen = tlen
    #    elements_sum = sum(a)
    #    assert tsum == elements_sum, " sum invariant: {:,} (root) - {:,} (elements) = {:,}\n{}\n{}". \
    #        format(tsum, elements_sum, tsum - elements_sum, get_tree_string(t), _dump)

# interface:
    def add(self, v):
        fv = self._f(v)
        #info(' add({:,} -> {:,})'.format(v, fv))
        #debug(get_tree_string(self.root))
        isAdded = self._add(fv)
        #assert self._find(self.root, fv)
        #info(' added:')
        #info(get_tree_string(self.root))
        #self._assert_invariants(self.root, self.lastlen + (1 if isAdded else 0))

    def delete(self, v):
        fv = self._f(v)
        #info(' delete({:,} -> {:,})'.format(v, fv))
        #debug(get_tree_string(self.root))
        isDeleted = self._delete(fv)
        #info(' after :')
        #info(get_tree_string(self.root))
        #self._assert_invariants(self.root, self.lastlen - (1 if isDeleted else 0))

    def find(self, v):
        fv = self._f(v)
        #info(' find({:,} -> {:,})'.format(v, fv))
        found = self._find(self.root, fv)
        #if found:  # to make sure splay correct
            #self._assert_invariants(self.root, self.lastlen)
        #info(' after find:')
        #info(get_tree_string(self.root))
        return found != None

    def sum(self, l, r):
        global _dump
        """
            Посчитать сумму всех элементов множества, попадающих в отрезок [f(l),f(r)].
        """
        l2 = self._f(l)
        r2 = self._f(r)
        #info(' sum({:,} -> {:,}, {:,} -> {:,})'.format(l, l2, r, r2))
        #debug(get_tree_string(self.root))
        #assert l2 <= r2, \
            #"""should not be given an invalid arguments so lastsum is wrong:
            ##s={:,}, f({:,}) = {:,} <= {:,} = f({:,})\n{}\n{}""" \
            #.format(self.lastsum, l, l2, r2, r, get_tree_string(self.root), _dump)
        s = self._sum(l2, r2)
        #info(' after sum:')
        #info(get_tree_string(self.root))
        #self._assert_invariants(self.root, self.lastlen)
        self.lastsum = s
        return s
# end interface

    def _f(self, v):
        task_constant =  1000000001
        return (self.lastsum + v) % task_constant

    def _add(self, k):
        """
            Goes to the empty place to insert new node or updates root
        """
        #assert k >= 0
        isAdded = True
        z = Node(k)
        if self.root == None:
            self.root = z
        else:
            # go to the first empty place, insert a new node and splay it to the top:
            # should take O(log(n))
            v = self.root
            while True:
                if v.key == k:
                    v.refresh_sum()  # to erase added sums
                    z = v  # to splay anyway
                    isAdded = False
                    break
                elif v.key < k:
                    """ k = 51
                       50
                     34     65
                    |  |   |  |
                    """
                    v.sum += k
                    if v.r == None:
                        v.r = z
                        z.p = v
                        break
                    v = v.r
                else:
                    v.sum += k
                    #assert v.key > k
                    if v.l == None:
                        v.l = z
                        z.p = v
                        break
                    v = v.l
            if z:
                self._splay(z)
                self.root = z

        return isAdded

    def _delete(self, k):
        # find k:
        v = self.root
        while v != None:
            if v.key == k:
                break  # found
            elif v.key < k:
                v = v.r
            else:
                v = v.l
        if not v or v.key != k:
            return False

        self._splay(v)  # to put at root
        #debug(' (delete) after splay:\n{}'.format(get_tree_string(v)))
        assert v.p == None

        # link left and right trees and remove link to v:

        vl = v.l
        vr = v.r
        if vl:
            vl.p = None
        if vr:
            vr.p = None
        self.root = self._merge(vl, vr)
        return True

    def _find(self, v, k):
        while v != None:
            if v.key == k:
                break  # found
            elif v.key < k:
                v = v.r
            else:
                v = v.l

        if not v or v.key != k:
            return None
        else:
            self._splay(v)
            self.root = v
            return v

    def _sum(self, l, r):
        global _dump
        """
        Посчитать сумму элементов попадающих в отрезок [l, r]
        t -> t1 < l <= t2
        t2 -> t3 <= r < t4
        t3 sum -> result
        t2 <- merge t3, t4
        t <- merge t1, t2
        """
        if not self.root:
            return 0
        root_sum = self.root.sum
        t1, t2 = self._split(self.root, l - 1)  # lt_l < l <= ge_l
        assert not t1 or not t1.p
        assert not t2 or not t2.p
        #self._assert_invariants(t1)
        #self._assert_invariants(t2)
        #debug("t1={}".format(get_tree_string(t1)))
        #debug("t2={}".format(get_tree_string(t2)))

        t3, t4 = self._split(t2, r)
        #debug("t3={}".format(get_tree_string(t3)))
        #debug("t4={}".format(get_tree_string(t4)))
        assert not t3 or not t3.p
        assert not t4 or not t4.p
        #self._assert_invariants(t3)
        #self._assert_invariants(t4)

        #t3key = None
        #if t3:
        #    t3key = t3.key
        res = t3.sum if t3 != None else 0

        # merge back to keep consistent:
        t2 = self._merge(t3, t4)
        #debug("t2={}".format(get_tree_string(t2)))
        #self._assert_invariants(t2)

        self.root = self._merge(t1, t2)
        #debug("root={}".format(get_tree_string(self.root)))
        #self._assert_invariants(self.root)
        #if root_sum > 0:
            #assert self.root.sum
            #assert root_sum == self.root.sum, "sum before {} - {} sum now = {}:{}".format(root_sum, self.root.sum, root_sum - self.root.sum)

        return res

    def _split(self, v, k):
        """
        Splits v into left <= k < right

            5
          3      7
        1   4   6   9
        k=3: returns (1 3 , 4 5 6 7 8)
        """
        if v == None:
            return (None, None)

        # find u, the greatest in those <= k:
        u = v
        while True:
            if u.key == k:
                break
            elif u.key < k:
                if not u.r:
                    break
                u = u.r
            else:
                if not u.l:
                    break
                u = u.l
        self._splay(u)
        assert not u.p, "should be root"

        if u.key <= k:
            ur = u.r
            assert not ur or ur.key > k
            if ur:
                ur.p = None
                u.r = None
                u.refresh_sum()
            return (u, ur)
        else:  # k < u.key
            ul = u.l
            assert not ul or ul.key <= k
            if ul:
                ul.p = None
                u.l = None
                u.refresh_sum()
            return (ul, u)

    def _merge_with_root(self, v, t1, t2):  # less than, greater than
        """
        Merges two trees
        """
        #assert v != None
        #assert t1 == None or t1.key < v.key
        #assert t2 == None or v.key < t2.key
        # left:
        if v.l:
            v.l.p = None
        v.l = t1
        if t1:
            if t1.p:
                if t1.p.l == t1:
                    t1.p.l = None
                else:
                    t1.p.r = None
            t1.p = v

        # right:
        if v.r:
            v.r.p = None
        v.r = t2
        if t2:
            if t2.p:
                if t2.p.l == t2:
                    t2.p.l = None
                else:
                    t2.p.r = None
            t2.p = v
        if v.r:
            v.r.refresh_sum(updateParents=False)
        if v.l:
            v.l.refresh_sum(updateParents=False)
        v.refresh_sum(updateParents=False)
        return v

    def _merge(self, t1, t2):
        """
        Сливает два дерева, поддерживая сумму для вершин.
        """
        t = None
        if not t1 or not t2 :
            t = t1 or t2
        else:
            assert t1.p == None
            assert t2.p == None
            #assert t1.key < t2.key
            t1_max = self._get_max(t1)
            #debug(" (merge) before splay t1_max:{}".format(get_tree_string(t1_max)))
            #assert t1_max != None
            #assert t1_max.r == None

            self._splay(t1_max)
            #debug(" (merge) after splay t1_max:{}".format(get_tree_string(t1_max)))
            assert not t1_max.p
            assert not t1_max.r
            t1_max.r = t2
            t2.p = t1_max
            t1_max.refresh_sum()
            t = t1_max
        return t

    def _get_max(self, v):
        while v and v.r:
            v = v.r
        return v

    def _transplant(self, u, v):
        """
        Transplants v at u's place
        """
        if u.p:
            if u.p.r == u:
                u.p.r = v
            else:  # if u.p.r == u:  # don't assert this as we can call it in rotate_left/right and there left/right children are changed
                u.p.l = v
        if v:
            v.p = u.p
        u.p = None

    def _left_rotate(self, u):
        """
           u
         A    v
            B   C
        A < u < B < v < C

        ->
              v
          u     C
        A   B
        """
        #assert u.r.p == u
        v = u.r
        u.r = v.l
        if u.r:
            u.r.p = u
        self._transplant(u, v)
        v.l = u
        v.l.p = v
        v.l.refresh_sum(updateParents=False)
        v.refresh_sum(updateParents=False)

    def _right_rotate(self, u):
        """
              u
          v     C
        A   B
        A < v < B < u < C

        to:
           v
         A    u
            B   C
        """
        #assert u.l.p == u
        v = u.l
        u.l = v.r
        if u.l:
            u.l.p = u
        self._transplant(u, v)
        v.r = u
        v.r.p = v
        v.r.refresh_sum(updateParents=False)
        v.refresh_sum(updateParents=False)

    def _splay(self, u):
        global _dump
        if not u or not u.p:
            return u
        # debug(' before splay at u={}:\n{}'.format(u.key, get_tree_string(u.p.p or u.p)))
        while u.p != None:
            if not u.p.p:
                if u == u.p.l:
                    self._right_rotate(u.p)
                elif u == u.p.r:
                    self._left_rotate(u.p)
                else:
                    assert False, "INVALID TREE"
            else:
                # zig-zig:
                if u == u.p.l and u.p == u.p.p.l:
                    self._right_rotate(u.p.p)
                    self._right_rotate(u.p)
                elif u == u.p.r and u.p == u.p.p.r:
                    self._left_rotate(u.p.p)
                    self._left_rotate(u.p)
                # zig-zag:
                elif u == u.p.l and u.p == u.p.p.r:
                    self._right_rotate(u.p)
                    self._left_rotate(u.p)
                elif u == u.p.r and u.p == u.p.p.l:
                    self._left_rotate(u.p)
                    self._right_rotate(u.p)
                else:
                    # should not get here:
                    assert False, ' INVALID TREE. u={}. Tree:\n{}\n{}'.format(u.key, get_tree_string(u.p.p or u.p), _dump)
        #debug(' after splay:\n' + get_tree_string(u))

    def __str__(self):
        return "Inorder:" + inorder(self.root)


n = int(input().strip())
#_dump += str(n) + "\n"
t = BstOfSum()
toPrintDump = False
for i in range(n):
    in_ = input()
    #_dump += in_ + "\n"
    call = in_.strip().split(' ')
    #info(' '.join(call))
    c = call[0]
    if c == '+':
        t.add(int(call[1]))
    elif c == '-':
        t.delete(int(call[1]))
    elif c == '?':
        print('Found' if t.find(int(call[1])) else 'Not found')
    elif c == 's':
        #if call[1] == '40279559':  # test #20
        #    toPrintDump = True
        print(t.sum(int(call[1]), int(call[2])))

if toPrintDump:
    pass
    #assert False, _dump
