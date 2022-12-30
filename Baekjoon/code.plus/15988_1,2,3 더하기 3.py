import sys
from sys import stdin

MOD = 1000000009
SIZE = 1000000


def solve(target):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if memo[target] != -1:
        return memo[target]

    res = 0
    for i in range(1, 4):
        res = (res + solve(target - i)) % MOD
    memo[target] = res
    return res


def solve2():
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(SIZE + 1):
        if dp[i] != 0:
            for x in range(1, 4):
                if i + x < SIZE:
                    dp[i+x] = (dp[i+x] + dp[i]) % 1000000009


memo = [-1] * (SIZE + 1)
dp = [0] * (SIZE + 1)
solve2()
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    print(dp[N])