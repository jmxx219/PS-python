from sys import stdin


def solve2():   # 테뷸레이션
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 3

    for i in range(2, N + 1):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

    return dp[N]


def solve(y, x):
    if y == N-1:
        return 1
    if y >= N:
        return 0
    if memo[y][x] != 0:
        return memo[y][x]

    memo[y][0] = (solve(y + 1, 0) + solve(y + 1, 1) + solve(y + 1, 2)) % MOD
    memo[y][1] = (solve(y + 1, 0) + solve(y + 1, 2)) % MOD
    memo[y][2] = (solve(y + 1, 0) + solve(y + 1, 1)) % MOD

    return memo[y][x]


MOD = 9901
N = int(stdin.readline())
memo = []
for _ in range(N):
    memo.append([0] * 3)
# print(solve2())
print(solve(0, 0) + solve(0, 1) + solve(0, 2))