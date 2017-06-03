import csv

crimeTypes = {}
with open('crimes.csv','r') as f :
    r = csv.reader(f)
    header = next(r)
    i = header.index('Primary Type')
    for row in r :
        name = row[i]
        if name not in crimeTypes :
            crimeTypes[name] = 0
        crimeTypes[name] += 1

M = ('',0)
for key in crimeTypes :
    if M[1] < crimeTypes[key] :
        M = (key, crimeTypes[key])
print(M[0])




