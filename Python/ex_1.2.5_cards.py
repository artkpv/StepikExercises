n = int(input())
k1 = list(map(int, input().split()))[1:]
k2 = list(map(int, input().split()))[1:]

k1.reverse()
k2.reverse()

prev_games = []

count = 0
winner = -1
while True:
    if len(k1) == 0:
        winner = 2
        break
    elif len(k2) == 0:
        winner = 1
        break
    if count > 1000:
        break
    # game:
    up1 = k1.pop()
    up2 = k2.pop()
    if up1 > up2:
        k1 = [up2] + k1
        k1 = [up1] + k1
    else:
        k2 = [up1] + k2
        k2 = [up2] + k2

    count += 1

if winner == -1:
    print(-1)
else:
    print(str(count), str(winner))
