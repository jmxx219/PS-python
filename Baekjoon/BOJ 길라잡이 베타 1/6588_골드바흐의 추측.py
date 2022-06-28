import math
from sys import stdin


def prime_list(N: int):
    sieve = [True] * N

    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False

    return sieve


def solve(n: int):
    bl = False

    for i in range(3, n):
        if prime[i] and prime[n - i]:
            bl = True
            print(f'{n} = {i} + {(n - i)}')
            break

    if not bl: print("Goldbach's conjecture is wrong.")


prime = prime_list(1000000)
while True:
    x = int(stdin.readline())
    if x == 0: break
    solve(x)