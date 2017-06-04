#! python3
"""
Ваша цель в данной задаче — реализовать структуру данных Rope.
Данная структура данных хранит строку и позволяет эффективно вы-
резать кусок строки и переставить его в другое место.
Формат входа. Первая строка содержит исходную строку S, вто-
рая — число запросов q. Каждая из последующих q строк задаёт
запростройкойчиселi,j,k иозначаетследующее:вырезатьпод-
строку S[i..j] (где i и j индексируются с нуля) и вставить её после
k-го символа оставшейся строки (где k индексируется с едини-
цы), при этом если k = 0, то вставить вырезанный кусок надо в
начало.
Формат выхода. Выведитеполученную(послевсехqзапросов)стро-
ку.
Ограничения. S содержит только буквы латинского алфавита. 
 1 ≤ |S| ≤ 300000;
 1 ≤ q ≤ 100000;
 0 ≤ i ≤ j ≤ n−1;
 0 ≤ k ≤ n−(j−i+1).
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
    def __init__(self, c):
        self.p = None
        self.l = None
        self.r = None
        self.c = c
        self.size = 1

    def isLeaf(self):
        return self.l == None and self.r == None

    def refresh_size(self):
        self.size = 1 + (self.l.size if self.l else 0) + (self.r.size if self.r else 0)


class BstRope:
    def __init__(self, s):
        self.lastsum = 0
        self.root = None
        self._split_common_child = None
        for i in range(len(s)):
            self._add(s[i], i + 1)
        self._splay(len(s) // 2)

    def _assert_invariants(self, t):
        tsize = t.size if t else 0
        elements_num = len(inorder(t))
        assert tsize == elements_num #, " tree invariant: root size = {:,} - {:,} (elements) = {:,}\n{}\n{}". \
            #format(tsum, elements_sum, tsum - elements_sum, get_tree_string(t), _dump)

# interface:

    def reorder(self, i, j, k):
        """
        Вырезать с i по j (c 0), вставить после k-го символа в строке, с вырезанным фрагментом
        1 1 2, hlelowrold -> hellowrold
        Ex.:
           abcdefghijklm, 4,5,1 -> aefbcdghijklm
        1 abcd efghijklm   split t  3  -> t1, t2
        2 abcd ef ghijklm  split t2 2  -> t3, t4
        3 abcdghijklm ef   merge t1 t4 -> t5
        4 a bcdghijklm ef  split t5 1  -> t6, t7
        5 aef bcdghijklm   merge t6, t3-> t8
        6 aefbcdghijklm    merge t8, t7 -> t
        """
        l = len(self.s)
        t = self._tree
        assert 0 <= i
        assert i <= j
        assert j < l
        assert 1 <= k
        assert k <= l
        if i == k:  # already at its place
            return
        t1, t2 = self._split(t, i - 1)
        t3, t4 = self._split(t2, j - i + 1)
        t5 = self._merge(t1, t4)
        t6, t7 = self._split(t5, k)
        t8 = self._merge(t6, t3)
        t = self._merge(t8, t7)
        self._tree = t
        return self._get_string(t)

# end interface

    def _add(self, c, k):
        """
            Goes to the empty place to insert new node or updates root
        """
        #assert k >= 0
        z = Node(c)
        if self.root == None:
            self.root = z
        else:
            v = self.root
            while True:
                if v.c == c:
                    raise 'add of a c should be only once'
                elif v.size < k:
                    if v.r == None:
                        v.r = z
                        z.p = v
                        z.refresh_sum()
                        break
                    v = v.r
                else:
                    #assert v.key > k
                    if v.l == None:
                        v.l = z
                        z.p = v
                        z.refresh_sum()
                        break
                    v = v.l


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
            if not le and not gt:  # common ancestor for border:
                self._split_common_child = v
            v = self._merge_with_root(v, gt, v.r)
            if le:
                le.refresh_sum(updateParents=False) 
            #debug("  _split({:,}, {:,}) -> {{{}}} and {{{}}}".format(v.key, k, inorder(le), inorder(v)))
            #self._assert_invariants(le)
            #self._assert_invariants(v)
            return (le, v)

        if v.key <= k:
            le, gt = self._split(v.r, k)
            v = self._merge_with_root(v, v.l, le)
            if gt:
                gt.refresh_sum(updateParents=False) 
            #debug("  _split({:,}, {:,}) -> {} and {}".format(v.key, k, inorder(v), inorder(gt)))
            #self._assert_invariants(v)
            #self._assert_invariants(gt)
            return (v, gt)

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
            #assert t1.key < t2.key
            t1_max = self._get_max(t1)
            #assert t1_max != None
            #assert t1_max.r == None

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
                #debug(' merge \n{}\n with \n {} \n t1_max={}' \
                    #.format(get_tree_string(t1), get_tree_string(t2), t1_max.key))

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
        left_border_common_child = self._split_common_child
        #self._assert_invariants(t1)
        #self._assert_invariants(t2)

        t3, t4 = self._split(t2, r)
        #self._assert_invariants(t3)
        #self._assert_invariants(t4)

        #t3key = None
        #if t3:
        #    t3key = t3.key
        res = t3.sum if t3 != None else 0

        # merge back to keep consistent:
        t2 = self._merge(t3, t4)
        #self._assert_invariants(t2)

        self.root = self._merge(t1, t2)
        #self._assert_invariants(self.root)
        #assert root_sum_at_start == (self.root.sum if self.root else 0)

        if left_border_common_child:
            self._splay(left_border_common_child)  # try to get common up
        return res

    def _get_max(self, v):
        while v and v.r:
            v = v.r
        return v

    def _translant_parent(self, u, v):
        """
        Transplants v at u's place 
        """
        #assert u
        if v and v.p:  # nullify v.p:
            if v.p.r == v:
                v.p.r = None
            elif v.p.l == v:
                v.p.l = None
            v.p = None
        if not u.p:
            if u == self.root:
                self.root = v
        else:
            if u.p.l == u:
                u.p.l = v
            elif u.p.r == u:  # don't assert this as we can call it in rotate_left/right and there left/right children are changed
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
        #assert u
        #assert u.r.p == u
        v = u.r

        u.r = v.l
        if u.r:
            u.r.p = u

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
        #assert u
        #assert u.l.p == u
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

    def _splay(self, k):
        # TODO: by k-order
        raise NotImplementedError()

        global _dump
        if not u or not u.p:
            return
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

    def _delete(self, v):
        if v == None:
            return

        self._splay(v)
        #assert self.root == v
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
        return ''.join(v.c for v in inorder(self.root))

s = input().strip()
q = int(input().strip())

rope = BstRope(s)

for query in range(q):
    i, j, k = [int(p) for p in input().strip().split(' ')]
    rope.reorder(i, j, k)
    info(' after query, i={} j={} k={}: {}'.format(i, j, k, str(rope)))

print(rope)





