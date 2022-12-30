from sys import stdin


def solve():
    if N == 1:
        return stairs[1]

    # dp[i][j]: i번째 계단을 올랐을 때, j개의 계단을 연속해서 밟은 점수 합의 최대(j는 1 or 2)
    dp = [[0] * 3 for _ in range(N+1)]
    dp[1][1] = stairs[1]
    dp[1][2] = 0
    dp[2][1] = stairs[2]
    dp[2][2] = stairs[1] + stairs[2]

    for k in range(3, N+1):
        dp[k][1] = max(dp[k-2][1], dp[k-2][2]) + stairs[k]
        dp[k][2] = dp[k-1][1] + stairs[k]

    return max(dp[N][1], dp[N][2])


N = int(stdin.readline())
stairs = [0] * (N + 1)
for i in range(1, N + 1):
    stairs[i] = int(stdin.readline())
# print(solve())
print(solve2())