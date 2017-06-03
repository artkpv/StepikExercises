class Stack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, i):
        self.s += [i]
        self.m.append(i if len(self.m) == 0 or self.m[-1] < i else self.m[-1])

    def pop(self):
        self.s.pop()
        self.m.pop()

    def max(self):
        print(self.m[-1])

n = int(input().strip())
stack = Stack()
for i in range(n):
    command = input().strip().split(' ')
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'max':
        stack.max()


