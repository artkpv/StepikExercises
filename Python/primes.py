
def is_prime(n, found) :
    for p in found :
        if n % p == 0 :
            return False
    return True

def primes() :
    n = 1
    primes = []
    while True :
        n += 1
        if is_prime(n, primes) :
            primes.append(n)
            yield n

import itertools
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
