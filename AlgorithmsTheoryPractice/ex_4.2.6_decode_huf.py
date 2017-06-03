import sys

class Node:
    def __init__(self, left=None, right=None, char=None):
        self.left = left
        self.right = right
        self.char = char
        pass

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, path, char):
        self._insert(path, char, self.root)

    def _insert(self, path, char, parent):
        assert(parent is not None)

        if path == '':
            parent.char = char
            return

        if path[0] == '0':
            if parent.left is None:
                parent.left = Node()
            self._insert(path[1:], char, parent.left)
        elif path[0] == '1':
            if parent.right is None:
                parent.right = Node()
            self._insert(path[1:], char, parent.right)
        else:
            raise 'invalid path'

    def get(self, path):
        return self._get(path, self.root)

    def _get(self, path, node):
        assert(node is not None)
        if path == '':
            return node.char

        assert(node.left is not None or node.right is not None)

        if path[0] == '0':
            return self._get(path[1:], node.left)
        elif path[0] == '1':
            return self._get(path[1:], node.right)

k, l = map(int, input().split(' '))
trie = Trie()
for i in range(k):
    letter, code = input().split(': ')
    trie.insert(code, letter)

encoded = input()
code = None
for c in encoded:
    if code is None:
        code = c
    else:
        code += c

    char = trie.get(code)
    if char:
        sys.stdout.write(char)
        code = None

