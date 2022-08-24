import copy
from sys import stdin


def LIS(start, resN):  # 시작 index 고정
    if memo[start] != -1:
        return memo[start]

    cntMax = 1
    nextMaxIndex = -1
    for i in range(start + 1, N):
        if nums[start] < nums[i]:
            nextCnt = LIS(i, resN) + 1
            if cntMax < nextCnt:
                cntMax = nextCnt
                nextMaxIndex = i

    reconstructArr[start] = nextMaxIndex
    memo[start] = cntMax
    return cntMax


def solve():
    resN = []
    cnt = 0
    for i in range(N):
        cnt = max(cnt, LIS(i, resN))
    print(reconstructArr)



N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
memo = [-1] * (N)
reconstructArr = [-1] * (N)
solve()
