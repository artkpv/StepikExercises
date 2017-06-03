line = input().strip()
if not line :
    print('')
    exit()

d = {}
for c in line:
    if c not in d :
        d[c] = 1
    else :
        d[c] += 1

ordered = sorted(d.keys())

left = ''.join(c * (d[c] // 2) for c in ordered if d[c] > 1)

result = left

loneChars = list([c for c in ordered if d[c] % 2 == 1])
if len(loneChars) > 0 :
    result += loneChars[len(loneChars) // 2 - 1]

if len(left) > 0 :
    result += ''.join((reversed(left)))

print(result)


