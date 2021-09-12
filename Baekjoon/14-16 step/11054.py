# 가장 긴 바이토닉 부분 수열
from sys import stdin


def solve(nums: list[int]) -> int:
    dp_increase = [0 for _ in range(N)]
    dp_decrease = [0 for _ in range(N)]

    for i in range(N):
        tmp = 0
        for j in range(i):
            if nums[j] < nums[i]:
                tmp = max(tmp, dp_increase[j])
        dp_increase[i] = tmp + 1

    for i in range(N - 1, -1, -1):
        tmp = 0
        for j in range(N - 1, i, -1):
            if nums[j] < nums[i]:
                tmp = max(tmp, dp_decrease[j])
        dp_decrease[i] = tmp + 1

    max_n = 0
    for i in range(N):
        dp_increase[i] = dp_increase[i] + dp_decrease[i] - 1
        max_n = max(max_n, dp_increase[i])
    return max_n


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(solve(nums))



