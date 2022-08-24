from collections import Counter
from sys import stdin


def canEatCandyCnt():
    res = 0

    for y in range(N):
        cnt = 0
        for x in range(1, N):
            if candy[y][x-1] == candy[y][x]:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)

    for x in range(N):
        cnt = 0
        for y in range(1, N):
            if candy[y-1][x] == candy[y][x]:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)
    return res + 1


def solve():
    cnt = 0

    for y in range(N):
        for x in range(1, N):
            if candy[y][x-1] != candy[y][x]:
                candy[y][x-1], candy[y][x] = candy[y][x], candy[y][x-1]
                cnt = max(cnt, canEatCandyCnt())
                candy[y][x-1], candy[y][x] = candy[y][x], candy[y][x-1]

    for x in range(N):
        for y in range(1, N):
            if candy[y-1][x] != candy[y][x]:
                candy[y-1][x], candy[y][x] = candy[y][x], candy[y-1][x]
                cnt = max(cnt, canEatCandyCnt())
                candy[y-1][x], candy[y][x] = candy[y][x], candy[y-1][x]

    return cnt


# C: 빨간색, P: 파란색, Z: 초록색, Y: 노란색
N = int(stdin.readline())

candy = []
for _ in range(N):
    candy.append(list(stdin.readline().rstrip()))

print(solve())