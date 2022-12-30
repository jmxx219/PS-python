from sys import stdin


def solve():
    dp = [[0, 0, 0] for _ in range(N)]

    dp[0][0] = houses[0][0]
    dp[0][1] = houses[0][1]
    dp[0][2] = houses[0][2]

    for k in range(1, N):
        dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + houses[k][0]
        dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + houses[k][1]
        dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + houses[k][2]

    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])


N = int(stdin.readline())
houses = [] # 빨강, 초록, 파랑
for _ in range(N):
    houses.append(list(map(int, stdin.readline().split())))

print(solve())