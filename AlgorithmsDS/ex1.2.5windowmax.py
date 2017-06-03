'''
    Ex. 1.2.5 at https://stepik.org/lesson/Задачи-41234/step/5
'''

class MStack:
    def __init__(self):
        self.s = []
        self.m = []

    def size(self):
        return len(self.s)

    def push(self, i):
        self.s += [i]
        self.m.append(i if len(self.m) == 0 or self.m[-1] < i else self.m[-1])

    def pop(self):
        self.m.pop()
        return self.s.pop()

    def max(self):
        return self.m[-1] if len(self.m) != 0 else -1


class MQueue:
    def __init__(self, size):
        self.left = MStack()
        self.right = MStack()
        self.capacity = size

    def enqueue(self, i):
        if self.left.size() + self.right.size() == self.capacity:
            self.dequeue()
        self.left.push(i)

    def dequeue(self):
        if self.right.size() == 0:
            while self.left.size() > 0:
                self.right.push(self.left.pop())
        self.right.pop()

    def size(self):
        return self.left.size() + self.right.size()

    def max(self):
        return max(self.left.max(), self.right.max())


n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
m = int(input().strip())
mqueue = MQueue(m)
for i in range(n):
    mqueue.enqueue(a[i])
    if mqueue.size() == m:
        print(mqueue.max())
