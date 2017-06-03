import os, csv, re


count = 0
directory = 'data'
for d in os.walk(directory) :
    for csvName in (f for f in d[2] if f.endswith('csv')) :
        with open(d[0] + '/' + csvName, 'r') as csvFile :
            r = csv.reader(csvFile)
            headers = [n.lower() for n in next(r)]
            if 'pet' in headers :
                i = headers.index('pet')
                cats = 0
                dogs = 0
                for l in r :
                    val = l[i].strip().lower()
                    if val == 'cat' :
                        cats += 1
                    elif val == 'dog' :
                        dogs += 1
                if cats < dogs :
                    count += 1


print(count)





