"""
https://stepik.org/lesson/Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-27314/step/5?course=%D0%AD%D0%BA%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD-%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B9-%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D0%B8&unit=12620
"""

n, k = map(int, input().split())
leftwall = input()
rightwall = input()
walls = (leftwall,rightwall)

"""
Wall:
00 X-
00 -X
00 -X
00 X-
00 --
00 -X
10 --

Array:
10
00

"""
f = []
for i in range(n + 1) :
    f.append([0,0])
f[0][0] = 1

print('start field:',f)

def validate(i, j) :
    return i >= 0 and j >= 0 and i < len(f) and j < len(f[0])

def union(i, j, i2, j2) :
    """
    unions areas that was reached before
    """
    if not (validate(i, j) and validate(i2, j2)) :
        return

    first = f[i][j]
    second = f[i2][j2]

    if i == i2 and j == j2 and f[i][j] == 0 :
        f[i][j] = 10
        return
    f[i2][j2] = f[i][j]

    for k in range(len(f)) :
        for p in range(len(f[k])) :
            if f[k][p] == second and f[k][p] != 0 :
                f[k][p] = first

for i in range(len(walls)) :
    for j in range(len(walls[i])) :
        v = walls[i][j]
        if v == 'X' :
            continue
        union(i, j, i, j)

        if j > 0 and walls[i][j - 1] == '-' :
            union(i, j, i, j - 1) # moves down

        if validate(i, j + 1) and walls[i][j + 1] == '-' :
            union(i, j, i, j + 1) # moves up

        if validate(i, j+ k) and walls[(i + 1) % 2][j + k] == '-' :
            union(i, j, (i + 1) % 2, j + k) # jumps

        print('field:',f)


if f[0][n] == 1 or f[1][n] == 1 :
    print('YES')
else :
    print('NO')



