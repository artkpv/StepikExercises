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
Ограничения. S содержит только буквы латинского алфавита. 1 ≤
|S| ≤ 300000;1 ≤ q ≤ 100000;0 ≤ i ≤ j ≤ n−1;0 ≤ k ≤ n−(j−i+1).
"""

class Node:
    def __init__(self, char):
        self.char = char
        self.l = None
        self.r = None
        self.p = None
        self.size = 1

    @property
    def ikey(self):  # indirect key
        return (self.l.size if self.l else 0) + 1


class Rope:
    def __init__(self, s):
        # init by char and make it balanced
        self.s = s
        self._tree = None  # TODO

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
        t1, t2 = self.split(t, i - 1)
        t3, t4 = self._split(t2, j - i + 1)
        t5 = self._merge(t1, t4)
        t6, t7 = self._split(t5, k)
        t8 = self._merge(t6, t3)
        t = self._merge(t8, t7)
        self._tree = t
        return self._get_string(t)

    def _get_string(self, v):
        if not v:
            return ""
        s = ""
        s += self._get_string(v.left)
        s += v.char
        s += self._get_string(v.right)
        return s

    def _merge(self, t1, t2):
        # how?
        if not t1:
            return t2
        if not t2:
            return t1
        t1_max = self._get_max(t1)
        if t1 == t1_max:
            assert t1.right == None
            t1.right = t2
            # todo update sizes?
            return t1
        else:
            self._delete(t1_max)  # should update sizes
            t3 = self._merge_with_root(t1_max, t1, t2)  # should update sizes
            return t3

    def _delete(self, v):
        if not v:
            return

        if not v.left or not v.right:
            if v.p == None:

            self._transpose(
        pass

    def _merge_with_root(self, v, t1, t2):
        pass

    def _split(self, t, k):
        """ 
        Splits into: t1 <= k < t2. k - a indirect key, the order number of a char.
        """
        pass

    def _get_max(v):
        while v and v.right:
            v = v.right
        return v

s = input().strip()
q = int(input().strip())

rope = Rope(s)
for query in range(q):
    i, j, k = [int(p) for p in input().strip().split(' ')]
    rope.reorder(i, j, k)

print(rope)





