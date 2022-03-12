from sys import stdin


def solve(target, index, i):
    if index == 3 and target <= m:
        return target
    if index > 3 or target > m or i >= len(nums):
        return 0
    return max(solve(target + nums[i], index + 1, i + 1), solve(target, index, i + 1))


n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
print(solve(0, 0, 0))
