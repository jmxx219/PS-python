import math
import sys
from sys import stdin

sys.setrecursionlimit(10 ** 8)

INF = 987654321


def solve2(): # dp 테뷸레이션
    dp = [x for x in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N_sqrt + 1):
            if dp[i] > dp[i - j*j] + 1:
                dp[i] = dp[i - j*j] + 1

    return dp[N]


def solve(target): # dp 메모이제이션
    if target == 0:
        return 0
    elif target < 0:
        return INF

    if memo[target] != -1:
        return memo[target]

    res = INF
    for i in range(1, N_sqrt + 1):
        # res = min(res, solve(target - i * i)+1) => 더 느림(시간 초과)
        if res > solve(target - i*i) + 1:
            res = solve(target - i*i) + 1

    memo[target] = res
    return res


N = int(stdin.readline())
N_sqrt = int(math.sqrt(N))
memo = [-1] * (N + 1)
print(solve(N))
# print(solve2())