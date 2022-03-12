from sys import stdin


def solve():
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


str1 = stdin.readline().strip()
str2 = stdin.readline().strip()
print(solve())