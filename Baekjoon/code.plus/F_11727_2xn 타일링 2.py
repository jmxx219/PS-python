from sys import stdin


def solve():
    if N == 1:
        return 1
    elif N == 2:
        return 3

    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2
    return dp[N] % 10007


N = int(stdin.readline().rstrip())
print(solve())