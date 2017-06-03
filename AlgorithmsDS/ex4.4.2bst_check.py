'''
https://stepik.org/lesson/Задачи-45970/step/2?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=24123
'''

class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.upper = right.key if right is not None else None
        self.lower = left.key if left is not None else None
        self.key = key

class BSTWithCheck:

    def __init__(self, n):
        self.a = [None for i in range(n)]  # vertices by index
        if n > 0:
            # add empty root:
            self.root = Node()  # tree
            self.a[0] = self.root

    def insert_key_by_index(self, index, key, left_index, right_index):
        assert(len(self.a) > index)
        node = self.a[index]
        node.key = key
        if node.lower is not None and not node.lower < key:
            node.key = None
            return False
        if node.upper is not None and not key < node.upper:
            node.key = None
            return False
        # else valid so add this:
        if left_index != None:
            left = Node(parent=node)
            left.upper = node.key
            left.lower = node.lower
            node.left = left
            self.a[left_index] = left
        if right_index != None:
            right = Node(parent=node)
            right.lower = node.key
            right.upper = node.upper
            node.right = right
            self.a[right_index] = right
        return True


n = int(input().strip())
bst = BSTWithCheck(n)
for index in range(n):
    key, left, right = [int(j) for j in input().strip().split(' ')]
    isInserted = bst.insert_key_by_index(index,
                            key,
                            left if left != -1 else None,
                            right if right != -1 else None)
    if not isInserted:
        print('INCORRECT')
        exit()

print('CORRECT')  # as all inserted
