from requests import get
import sys

while True :
    line = sys.stdin.readline()
    if not line or not line.strip() :
        break
    num = int(line)
    r = get('http://numbersapi.com/{}/math?json=true'.format(num))
    data = r.json()
    if data['found'] :
        print('Interesting')
    else :
        print('Boring')
