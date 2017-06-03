# python3

"""
https://stepik.org/lesson/Обзор-13262/step/5
У вас есть примитивный калькулятор, который умеет выполнять всего три операции
с текущим числом xx: заменить xx на 2x2x, 3x3x или x+1x+1. По данному целому
числу 1≤n≤1051≤n≤105 определите минимальное число операций kk, необходимое,
чтобы получить nn из 1. Выведите kk и последовательность промежуточных чисел.
"""

n = int(input())

INF = 999999
d = [INF, 0]  # min steps to get i number

for i in range(2, n + 1):
    min_ = min(d[i-1],
               d[i//2] if i % 2 == 0 else INF,
               d[i//3] if i % 3 == 0 else INF)
    d += [min_ + 1]

print(d[n])

steps = []
i = n
while len(steps) < d[n]:
    steps += [i]
    min_ = min(
        d[i-1],
        d[i//2] if i % 2 == 0 else INF,
        d[i//3] if i % 3 == 0 else INF)
    if min_ == d[i-1]:
        i = i - 1
    elif i % 2 == 0 and min_ == d[i//2]:
        i = i // 2
    elif i % 3 == 0 and min_ == d[i//3]:
        i = i // 3
steps += [1]

print(' '.join(str(j) for j in reversed(steps)))
