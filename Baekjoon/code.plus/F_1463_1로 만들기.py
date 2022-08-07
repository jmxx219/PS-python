import sys
from sys import stdin
sys.setrecursionlimit(10**6)

INF = 987654321


def solve(N): # 재귀 -> 메모리 초과
    if N == 1: return 0
    if N < 1: return INF
    if memo[N] != -1: return memo[N]

    res = INF

    if N % 3 == 0:
        res = min(res, solve(N // 3))

    if N % 2 == 0:
        res = min(res, solve(N // 2))

    res = min(res, solve(N - 1))

    memo[N] = res + 1

    return memo[N]


n = int(stdin.readline())
memo = [-1] * (n + 1)
print(solve(n))
print(memo)
