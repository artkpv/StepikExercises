"""
Целое положительное число называется простым, если оно делится только на единицу и на само себя. Единица не является простым числом.
Целое положительное число называется составным, если оно не является простым.

Пример простых чисел
2, 3, 5, 7, 11, 31

Пример составных чисел
1, 4, 6, 8, 34

Вашей программе на вход подается число ﻿nn (4≤n≤1004≤n≤100).

Выведите все числа, не превосходящие nn, которые можно представить в виде произведения двух простых чисел. Числа следует выводить в возрастающем порядке.

Sample Input 1:
4
Sample Output 1:
4

Sample Input 2:
18
Sample Output 2:
4 6 9 10 14 15
"""

import sys
n = int(input())
primes = [2, 3]
result = []
for i in range(4, n + 1) :
    first = None
    for p in primes:
        if i % p == 0 :
            first = p
            break

    if not first :
        primes.append(i)
        continue

    quotient = i / first
    for p in primes:
        if quotient / p == 1 :
            result.append(i)
            break

print(' '.join(str(i) for i in result))




