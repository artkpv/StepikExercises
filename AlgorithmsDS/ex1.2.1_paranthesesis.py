_str = input()
s = []
size = 0
opens = r'([{'
closes = r')]}'
for i in range(len(_str)):
    c = _str[i]
    if c in closes:
        if len(s) == 0 or s.pop()[0] != opens[closes.index(c)]:
            print(i + 1)  # 1 based
            exit()
    elif c in opens:
        s.append((c, i))
if len(s) > 0:
    print(s.pop()[1] + 1)  # 1 based
    exit()

print('Success')



