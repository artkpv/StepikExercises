"""
https://stepik.org/lesson/Задачи-41560/step/2?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=20013

"""

from heapq import heappush as hpush, heappop as hpop
import pdb
import logging as log
from logging import debug
log.basicConfig(level=log.INFO, format='%(message)s')


class Computer:
    def __init__(self, n):
        assert(n > 0)
        self.processors = []
        for i in range(n):
            hpush(self.processors, (0, i))

    def add_task(self, task):
        # take next processor that become free and add task weight to it = it works for this time at this task
        #debug('adding task %s', task)
        processor = hpop(self.processors) if any(self.processors) else None
        task.time = processor[0]
        task.processor = processor[1]
        processor = (processor[0] + task.weight, processor[1])
        hpush(self.processors, processor)

    def __repr__(self):
        return str.format('comp at {}\n procs: {} \n tasks: {}', self.now, self.processors, self.tasks)

class Task:
    def __init__(self, t, order):
        self.order = order
        self.weight = t
        self.time = None
        self.processor = None

    def __repr__(self):
        return str.format('({}, {}, {})', self.weight, self.time, self.processor)

n, t = [int(i) for i in input().strip().split(' ')]
taskTimes = input().strip().split(' ')
tasks = []
for i in range(len(taskTimes)):
    tasks += [Task(int(taskTimes[i]), i)]
comp = Computer(n)
for t in tasks:
    comp.add_task(t)
for t in tasks:
    print(t.processor, t.time)


