from requests import get
from re import findall,search

count = 0
url = input()
r = get(url)
if r.status_code != 200 or not 'html' in r.headers['Content-Type'] :
    print('0')
    exit()

for m in findall(r'(?i)<\s*img [^>]*src\s*=\s*[\'"]?([^\'"]+)[\'"]? ?[^>]*>', r.text) :
    imgAns = get(m)

    if imgAns.status_code == 200 :
        ct = ''
        for h in imgAns.headers.keys() :
            if h.lower() == 'content-type' :
                ct = imgAns.headers[h]

        if search('(?i)image', ct) :
            count += 1

print(count)

