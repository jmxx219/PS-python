from sys import stdin


def solve():
    dp = [[1] * 10 for _ in range(N + 2)]
    for i in range(2, N + 2):
        for j in range(1, 10):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 10007

    return dp[N+1][9]


N = int(stdin.readline())

print(solve())