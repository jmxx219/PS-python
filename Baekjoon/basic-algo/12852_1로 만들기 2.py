from sys import stdin


def solve():
    dp = [0] * (N+1)
    tmp = [0] * (N+1)

    dp[1] = 0

    for k in range(2, N+1):
        dp[k] = dp[k-1] + 1
        tmp[k] = k-1
        if k % 3 == 0:
            if dp[k] > dp[k//3]:
                dp[k] = dp[k//3] + 1
                tmp[k] = k//3
        if k % 2 == 0:
            if dp[k] > dp[k // 2]:
                dp[k] = dp[k // 2] + 1
                tmp[k] = k // 2
    print(dp[N])

    if N != 1:
        print(N, end=' ')
        i = N
        while tmp[i] != 1:
            print(tmp[i], end=' ')
            i = tmp[i]
    print(1, end=' ')


N = int(stdin.readline())
solve()