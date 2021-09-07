from sys import stdin


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a < b < c :
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return dp[a][b][c]


def w2(a: int, b: int, c: int):
    if (a, b, c) in memo.keys():
        return memo[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = w(20, 20, 20)
    elif a < b < c:
        memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return memo[(a, b, c)]


memo = {}
dp = [[[-1] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")





