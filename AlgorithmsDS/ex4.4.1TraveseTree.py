import sys
class Node:
    def __init__(self, k, l, r):
        self.k = k
        self.l = l
        self.r = r

def print_inorder(a, v):
    s = ''
    if v.l != -1:
        s += print_inorder(a, a[v.l])
    s += str(v.k) + ' '
    if v.r != -1:
        s += print_inorder(a, a[v.r])
    return s

def print_preorder(a, v):
    s = str(v.k) + ' '
    if v.l != -1:
        s += print_preorder(a, a[v.l])
    if v.r != -1:
        s += print_preorder(a, a[v.r])
    return s

def print_postorder(a, v):
    s = ''
    if v.l != -1:
        s += print_postorder(a, a[v.l])
    if v.r != -1:
        s += print_postorder(a, a[v.r])
    s += str(v.k) + ' '
    return s

n = int(input().strip())
a = [None for i in range(n)]
for i in range(n):
    key, left_inx, right_inx = [int(j) for j in input().strip().split(' ')]
    a[i] = Node(key, left_inx, right_inx)

print(print_inorder(a, a[0]))
print(print_preorder(a, a[0]))
print(print_postorder(a, a[0]))
