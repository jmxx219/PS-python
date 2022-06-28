import math
from sys import stdin


def eratos(N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i]:
            for j in range(i + i, N + 1, i):
                sieve[j] = False

    return sieve


def solve(n):
    if n < r: return sieve[n]

    for p in prime_list:
        if n % p == 0: return False

    return True


r = 2 * pow(10, 6)
sieve = eratos(r)
prime_list = [i for i in range(2, r) if sieve[i]]

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int, stdin.readline().split())
    N = A + B

    if N < 4: print("NO")
    elif N % 2 == 0: print("YES") # 4이상의 모든 짝수는 두 소수의 합으로 구할 수 있음(골드바흐의 추측)
    else:
        if solve(N - 2): print("YES")
        else: print("NO")