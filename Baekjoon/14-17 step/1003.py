def solve(n: int):
    zeroCnt = [1, 0]
    oneCnt = [0, 1]

    if n == 0:
        print(zeroCnt[0], zeroCnt[1])
    elif n == 1:
        print(oneCnt[0], oneCnt[1])
    else:
        for i in range(2, n+1):
            zeroCnt.append(zeroCnt[i-1] + zeroCnt[i-2])
            oneCnt.append(oneCnt[i-1] + oneCnt[i-2])
        print(zeroCnt[n], oneCnt[n])


def solve2(n: int):
    dp = [[1, 0], [0, 1]]

    if n == 0:
        print(dp[0][0], dp[0][1])
    elif n == 1:
        print(dp[1][0], dp[1][1])
    else:
        for i in range(2, n+1):
            dp.append([dp[i-2][0] + dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
        print(dp[n][0], dp[n][1])


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        solve2(n)