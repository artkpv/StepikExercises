import sys
import re

openRe = re.compile(r'\(+(\s+\()*')
closeRe = re.compile(r'\)+(\s+\))*')
wordRe = re.compile(r'\w')
notParanRe = re.compile(r'[^\(\)]')

while True:
    l = sys.stdin.readline().strip()
    if not l:
        break

    # NOT RECURSIVE !!!! FUCK !!! Several hours on recursion!
    if re.search(r'\([^\(\)]*\w[^\(\)]*\)', l):
        print(l)

    continue

    #print(repr(l))
    pos = 0
    while pos < len(l):
        #print(' pos=' + str(pos))
        start = openRe.search(l, pos)
        if not start:
            #print(' no start paran.')
            break

        end = closeRe.search(l, start.end(0))
        if not end:
            #print(' no end paran.')
            break

        #print(l[start.start(0):end.end(0)])

        if not wordRe.search(l, start.end(0), endpos=end.start(0)) \
                or openRe.search(l, start.end(0), endpos=end.start(0)) \
                or closeRe.search(l, start.end(0), endpos=end.start(0)):
            pos += end.end(0)
            #print(' no words inside')
            continue

        n = len(re.findall('\(', start.group(0)))
        m = len(re.findall('\)', end.group(0)))
        #print(' n,m =' + str(n) + ' ' + str(m))
        if n == m:
            #print(' found')
            print(l)
            break

        pos += start.end(0)
