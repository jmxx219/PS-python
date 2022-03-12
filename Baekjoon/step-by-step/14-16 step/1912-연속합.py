# 연속합 - 동적 계획법
from sys import stdin


def solve():
    sums = [0] * N
    sums[0] = nums[0]

    for i in range(1, N):
        sums[i] = max(nums[i], sums[i - 1] + nums[i])

    return max(sums)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(solve())