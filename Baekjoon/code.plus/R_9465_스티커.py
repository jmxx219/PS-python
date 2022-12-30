from sys import stdin


def solve():
    if n == 1:
        return max(dp[0][0], dp[1][0])

    else:
        dp[0][1] += dp[1][0]  # 10 + 01
        dp[1][1] += dp[0][0]  # 00 + 11

        for i in range(2, n):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

        return max(dp[0][n - 1], dp[1][n - 1])


T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    dp = [list(map(int, stdin.readline().split())) for __ in range(2)]
    print(solve())

