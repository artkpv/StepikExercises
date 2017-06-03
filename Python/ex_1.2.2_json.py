# python3

import json, os

count = 0
for d in os.walk('.\\data'):
    for f in d[2]:
        if not f.endswith('json'):
            continue
        with open(d[0]+'\\' + f, 'r') as fp:
            data = json.load(fp)

        isHuman = False
        for k in data:
            if k and k.lower().strip() == 'kind' and data[k].lower() == 'human':
                isHuman = True
        if not isHuman :
            continue
        isGrown = False
        for k in data:
            if k and k.lower().strip() == 'age' and int(data[k]) >= 18:
                isGrown = True
        if isGrown :
            count += 1


print(count)
