from sys import stdin


def solve(target, cnt):
    if cnt == 0 and target == 0:
        return 1
    elif cnt < 0:
        return 0
    elif target < 0:
        return 0

    if memo[cnt][target] != -1:
        return memo[cnt][target]

    res = 0
    for i in range(N + 1):
        res += solve(target - i, cnt - 1)

    memo[cnt][target] = res % 1000000000
    return memo[cnt][target]


def solve2(target, cnt):
    if cnt == 1 or target == 0:
        return 1

    if memo[cnt][target] != -1:
        return memo[cnt][target]

    res = 0
    for i in range(target + 1):
        res += solve(i, cnt - 1)

    memo[cnt][target] = res % 1000000000
    return memo[cnt][target]


def solve3():
    dp = [[0] * (N+1) for _ in range(K+1)]

    for x in range(N+1):
        dp[1][x] = 1

    for y in range(1, K+1):
        for x in range(N+1):
            for k in range(x+1):
                dp[y][x] = (dp[y][x] + dp[y-1][x-k]) % 1_000_000_000

    return dp[K][N]


def solve4():
    dp = [[0] * (N+1) for _ in range(K+1)]

    for x in range(N+1):
        dp[1][x] = 1

    for y in range(1, K+1):
        for x in range(N+1):
            dp[y][x] = (dp[y][x-1] + dp[y-1][x]) % 1_000_000_000

    return dp[K][N]


N, K = map(int, stdin.readline().split())
memo = []
for _ in range(K + 1):
    memo.append([-1] * (N + 1))
# print(solve(N, K))
# print(solve2(N, K))
print(solve3())