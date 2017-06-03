import sys
sys.setrecursionlimit(50000)

class Package:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration
        self.start = -1

    def __repr__(self):
        return str((self.arrival, self.duration, self.start))

class Processor:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.now = 0

    def receive(self, p):
        # print('receive(', p, ')')
        self._process(p.arrival - self.now)  # trigger passed events
        if len(self.queue) < self.size:
            self.queue += [p]  # else rejected

    def _process(self, passed):  # time passed
        # print('_process(', passed, ') now=', self.now, ' q=', self.queue)
        if len(self.queue) == 0:
            self.now += passed
            return
        p = self.queue[0]

        if p.arrival <= self.now + passed:
            if p.start == -1:
                p.start = max(self.now, p.arrival)

            if p.duration <= passed:  # done with this package
                self.queue.pop(0)
                self.now += p.duration
                passed -= p.duration
                self._process(passed)
            else:  # didn't have time to finish current package
                p.duration -= passed
                self.now += passed

    def finish(self):  # infinitely process packages till they end up
        SOME_LARGE_TIME = 999999
        while len(self.queue) != 0:
            self._process(SOME_LARGE_TIME)


size, n = map(int, input().strip().split(' '))
processor = Processor(size)
packages = []
for i in range(n):
    arrival, duration = map(int, input().strip().split(' '))
    p = Package(arrival, duration)
    packages += [p]
    processor.receive(p)

processor.finish()

for p in packages:
    print(p.start)
