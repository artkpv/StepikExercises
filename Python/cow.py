import os

files = os.listdir('cow')
loses = {}
for f in files :
    name = f[0: f.find('.')]
    if name not in loses :
        loses[name] = 0
    wins = [l.strip() for l in open('cow/' + f).readlines()]
    for w in wins :
        if w not in loses :
            loses[w] = 0
        loses[w] += 1

print('\n'.join(('{}:{}'.format(k, loses[k]) for k in sorted(loses, key=lambda i : loses[i]))))

