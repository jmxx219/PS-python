from sys import stdin


def LIS(start):  # 시작 index 고정
    if memo[start] != -1:
        return memo[start]

    cntMax = 1
    for i in range(start + 1, N):
        if nums[start] < nums[i]:
            cntMax = max(cntMax, LIS(i) + 1)
    memo[start] = cntMax
    return cntMax


def solve():
    res = 0
    for i in range(N):
        res = max(res, LIS(i))
    return res


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
memo = [-1] * (N)
print(solve())