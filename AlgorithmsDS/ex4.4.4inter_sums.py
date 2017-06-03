#! python3

import sys
sys.setrecursionlimit(50000)

_dump = ""

"""
https://stepik.org/lesson/Задачи-45970/step/4?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=24123

NEXT
- See first test. Fails on sum? deletion?

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
        debug(' refresh_sum {}'.format(self.key))
        self.sum = self.key
        self.sum += self.l.sum if self.l != None else 0
        self.sum += self.r.sum if self.r != None else 0
        if updateParents and self.p != None:
            self.p.refresh_sum()


class BstOfSum:
    def __init__(self):
        self.lastsum = 0
        self.root = None

    def _assert_invariants(self, t):
        tsum = t.sum if t else 0
        elements_sum = sum(inorder(t))
        assert tsum == elements_sum, " sum invariant: {:,} (root) - {:,} (elements) = {:,}\n{}\n{}". \
            format(tsum, elements_sum, tsum - elements_sum, get_tree_string(t), _dump)

# interface:
    def add(self, v):
        info(' add({:,} -> {:,})'.format(v, self._f(v)))
        debug(get_tree_string(self.root))
        self._add(self._f(v))
        self._assert_invariants(self.root)
        info(' added:')
        info(get_tree_string(self.root))

    def delete(self, v):
        info(' delete({:,} -> {:,})'.format(v, self._f(v)))
        debug(get_tree_string(self.root))
        found = self._find(self.root, self._f(v))
        if found:
            self._delete(found)
            info(' deleted:')
            info(get_tree_string(self.root))
        else:
            info(' not found')
        self._assert_invariants(self.root)

    def find(self, v):
        found = self._find(self.root, self._f(v))
        return found != None

    def sum(self, l, r):
        global _dump
        """
            Посчитать сумму всех элементов множества, попадающих в отрезок [f(l),f(r)].
        """
        l2 = self._f(l)
        r2 = self._f(r)
        info(' sum({:,} -> {:,}, {:,} -> {:,})'.format(l, l2, r, r2))
        debug(get_tree_string(self.root))
        assert l2 <= r2, \
            """should not be given an invalid arguments so lastsum is wrong: 
            s={:,}, f({:,}) = {:,} <= {:,} = f({:,})\n{}\n{}""" \
            .format(self.lastsum, l, l2, r2, r, get_tree_string(self.root), _dump)
        s = self._sum(l2, r2)
        info(' after sum:')
        info(get_tree_string(self.root))
        self._assert_invariants(self.root)
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
        assert k >= 0
        z = Node(k)
        if self.root == None:
            self.root = z
        else:
            v = self.root
            while True:
                if v.key == k:
                    z = v
                    break
                elif v.key < k:
                    if v.r == None:
                        v.r = z
                        z.p = v
                        z.refresh_sum()
                        break
                    v = v.r
                else:
                    assert v.key > k
                    if v.l == None:
                        v.l = z
                        z.p = v
                        z.refresh_sum()
                        break
                    v = v.l
            if z:
                self._splay(z)

            return z

    def _split(self, v, k):
        """
        Splits v into left <= k < right. Keeps sums only till v.

            5
          3      7
        1   4   6   9
        k=3: returns (1, 5..)
        """
        if v == None:
            return (None, None)

        if k < v.key :
            le, gt = self._split(v.l, k)
            v = self._merge_with_root(v, gt, v.r)
            if le:
                le.refresh_sum(updateParents=False) 
            #debug("  _split({:,}, {:,}) -> {{{}}} and {{{}}}".format(v.key, k, inorder(le), inorder(v)))
            return (le, v)

        if v.key <= k:
            le, gt = self._split(v.r, k)
            v = self._merge_with_root(v, v.l, le)
            if gt:
                gt.refresh_sum(updateParents=False) 
            #debug("  _split({:,}, {:,}) -> {} and {}".format(v.key, k, inorder(v), inorder(gt)))
            return (v, gt)

    def _merge_with_root(self, v, t1, t2):  # less than, greater than
        """
        Merges two trees 
        """
        assert v != None
        assert t1 == None or t1.key < v.key
        assert t2 == None or v.key < t2.key
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
            assert t1.key < t2.key
            t1_max = self._get_max(t1)
            assert t1_max != None
            assert t1_max.r == None

            # max is the root of t1:
            if t1_max == t1:
                t = t1
                t.r = t2
                if t2.p:
                    if t2.p.l == t2:
                        t2.p.l = None
                    else:
                        t2.p.r = None
                t2.p = t

            # max not the root of t1:
            else:
                debug(' merge \n{}\n with \n {} \n t1_max={}' \
                    .format(get_tree_string(t1), get_tree_string(t2), t1_max.key))

                parent = t1_max.p
                self._translant_parent(t1_max, t1_max.l)
                if parent and parent != t1:
                    parent.refresh_sum()
                t1_max.p = None
                t = self._merge_with_root(t1_max, t1, t2)
            if t:
                t.refresh_sum()
        return t

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
        root_sum_at_start = self.root.sum if self.root else 0
        t1, t2 = self._split(self.root, l - 1)  # lt_l < l <= ge_l
        self._assert_invariants(t1)
        self._assert_invariants(t2)

        t3, t4 = self._split(t2, r)
        self._assert_invariants(t3)
        self._assert_invariants(t4)

        res = t3.sum if t3 != None else 0

        # merge back to keep consistent:
        t2 = self._merge(t3, t4)
        self._assert_invariants(t2)

        self.root = self._merge(t1, t2)
        self._assert_invariants(self.root)
        assert root_sum_at_start == (self.root.sum if self.root else 0)
        return res

    def _get_max(self, v):
        while v and v.r:
            v = v.r
        return v

    def _translant_parent(self, u, v):
        """
        Transplants v at u's place 
        """
        assert u
        if not u.p:
            self._translant_parent(v, None)  # remove link
            if u == self.root:
                self.root = v
        else:
            if u.p.l == u:
                u.p.l = v
            elif u.p.r == u:
                u.p.r = v
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
        assert u
        assert u.r.p == u
        v = u.r

        u.r = v.l
        if v.l:
            v.l.p = u

        self._translant_parent(u, v)
        u.p = v

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
        assert u
        assert u.l.p == u
        v = u.l

        u.l = v.r
        if u.l:
            u.l.p = u

        self._translant_parent(u, v)
        u.p = v

        v.r = u
        v.r.p = v

        v.r.refresh_sum(updateParents=False)
        v.refresh_sum(updateParents=False)

    def _splay(self, u):
        global _dump
        if not u or not u.p:
            return
        debug(' before splay:\n' + get_tree_string(u.p.p or u.p))
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
        # debug(' after splay:\n' + get_tree_string(self.root))

    def _delete(self, v):
        if v == None:
            return

        self._splay(v)
        assert self.root == v
        newroot = self._merge(v.l, v.r)
        if newroot:  # can be null if v was root
            newroot.p = None
        self.root = newroot
        return

    def _find(self, v, k):
        r = None
        if v != None:
            if v.key == k:
                r = v
            elif v.key < k:
                r = self._find(v.r, k)
            elif k < v.key:
                r = self._find(v.l, k)
        if r:
            self._splay(r)
        return r

    def __str__(self):
        return "Inorder:" + inorder(self.root)


n = int(input().strip())
_dump += str(n) + "\n"
t = BstOfSum()
for i in range(n):
    in_ = input()
    _dump += in_ + "\n"
    call = in_.strip().split(' ')
    info(' '.join(call))
    c = call[0]
    if c == '+':
        t.add(int(call[1]))
    elif c == '-':
        t.delete(int(call[1]))
    elif c == '?':
        print('Found' if t.find(int(call[1])) else 'Not found')
    elif c == 's':
        print(t.sum(int(call[1]), int(call[2])))
