from requests import get
import requests
import re

ans = 0

body = requests.get(input()).text
for href in re.findall(r'<a\b[^>]*[^\'"]\bhref="(.*?)"[^>]*>', body):
    r = requests.get(href)
    if r.status_code == 404:
        ans += 1

print(ans)
exit()

# WHY THIS BREAKS???
atagre = re.compile(r'(?i)(</?a((\s+\w+(\s*=\s*(?:".*?"|\'.*?\'|[\^\'">\s]+))?)+\s*|\s*)/?>)')

def get_broken_links(text) :
    broken = []
    atags = atagre.findall(text)
    for atag in atags:
        for attr in atag:
            if attr.strip().lower().startswith('href'):
                link = attr[attr.index('=')+1:].strip('\'"')
                r = get(link)
                if r.status_code == 404:
                    broken += [link]
                break
    print(len(broken))

url = input().strip()
r = get(url)
assert r.status_code == 200
get_broken_links(r.text)
