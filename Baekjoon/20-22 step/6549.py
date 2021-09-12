from sys import stdin


def solve(start, end, nums: list[int]) -> int:
    if start == end:
        return nums[start]

    mid = (start + end) // 2
    res = max(solve(start, mid, nums), solve(mid + 1, end, nums))
    lo = mid
    hi = mid + 1
    height = min(nums[lo], nums[hi])
    res = max(res, height * 2)

    while lo > start or hi < end:
        if lo > start and hi < end:
            if nums[lo - 1] < nums[hi + 1]:
                hi += 1
                height = min(height, nums[hi])
            else:
                lo -= 1
                height = min(height, nums[lo])
        elif lo > start:
            lo -= 1
            height = min(height, nums[lo])
        elif hi < end:
            hi += 1
            height = min(height, nums[hi])
        res = max(res, (hi - lo + 1) * height)

    return res


while True:
    nums = list(map(int, stdin.readline().split()))
    if nums[0] == 0:
        break
    print(solve(0, nums[0] - 1, nums[1:]))