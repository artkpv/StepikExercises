"""
aba
abacaba

0-4

"""

pattern = input().strip()
text = input().strip()

if len(pattern) > len(text):
    exit()  # no way to find this one

p = 1000000007
x = 263

def rollhash(hprev, leftChar, rightChar, xInPMinusOne, x, p):
    #return hprev + leftChar - rightChar
    r = (hprev - (rightChar * xInPMinusOne)%p)*x+leftChar
    r %= p
    return r

def hash(s, x, p):
    sum_ = 0
    for i in range(len(s)):
        #sum_ += ord(s[i])
        sum_ += (ord(s[i]) * pow(x, i, p))
        sum_ %= p
    return sum_

xInPMinusOne = pow(x, len(pattern) - 1, p)
patternHash = hash(pattern, x, p)
windowHash = hash(text[-len(pattern):], x, p)

indecies = []
i = len(text) - len(pattern)
while True:
    if windowHash == patternHash and text[i] == pattern[0] and text[i + len(pattern) - 1] == pattern[-1]:
        indecies += [i]
    i -= 1
    if i < 0:
        break
    windowHash = rollhash(windowHash, ord(text[i]), ord(text[i + len(pattern)]), xInPMinusOne, x, p)

indecies.reverse()
print(' '.join(str(i) for i in indecies))


