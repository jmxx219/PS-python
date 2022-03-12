# 가장 긴 증가하는 부분 수열
from sys import stdin


def solve():
    memo = [1] * N

    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                memo[i] = max(memo[i], memo[j] + 1)

    return max(memo)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(solve())
