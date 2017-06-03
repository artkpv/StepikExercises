# python3

"""
Failed test #9. Run time error:
Traceback (most recent call last):
  File "jailed_code", line 87, in <module>
    assert(leaf.left is None and leaf.right is None)
AssertionError
"""

from heap import MinHeap, Node

def get_trie(s):
    # get frequencies:
    frequencies = {}
    for c in s:
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1

    # build trie:
    heap = MinHeap()
    for c in frequencies:
        heap.insert(Node(frequencies[c], c))
    while heap.size() > 1:
        left = heap.extractmin()
        right = heap.extractmin()
        assert(left is not None)
        assert(right is not None)
        assert(left.frequency >= 0)
        assert(right.frequency >= 0)
        frequency = left.frequency + right.frequency
        node = Node(frequency)
        node.left = left
        node.right = right
        heap.insert(node)
    return heap.extractmin()


def build_codes(trie):
    codes = {}
    _build_codes(codes, trie, "")
    return codes


def _build_codes(codes, node, s):
    if node.isleaf():
        codes[node.char] = s if len(s) > 0 else '0'
        return
    _build_codes(codes, node.left, s + '1')
    _build_codes(codes, node.right, s + '0')


def encode(s):
    trie = get_trie(s)
    codes = build_codes(trie)
    encoded = ''
    for c in s:
        encoded += codes[c]

    out = ''
    out += '{} {}\n'.format(len(codes), len(encoded))
    for c in sorted(codes):
        out += '{}: {}\n'.format(c, codes[c])
    out += encoded + '\n'
    return out


import sys
encode(sys.stdin.read())
