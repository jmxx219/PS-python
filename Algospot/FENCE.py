from sys import stdin


def solve(start: int, end: int):
    if start == end:
        return fence[start]
    mid = (start + end) // 2

    res = max(solve(start, mid), solve(mid + 1, end))
    height = min(fence[mid], fence[mid+1])
    res = max(res, height * 2)

    lo = mid
    hi = mid + 1

    # while start < lo or hi < end:
    #     if start < lo and hi < end:
    #         if fence[lo - 1] < fence[hi + 1]:
    #             hi += 1
    #             height = min(height, fence[hi])
    #         else:
    #             lo -= 1
    #             height = min(height, fence[lo])
    #     elif start < lo:
    #         lo -= 1
    #         height = min(height, fence[lo])
    #     elif hi < end:
    #         hi += 1
    #         height = min(height, fence[hi])
    #     res = max(res, height*(hi-lo+1))

    while start < lo or hi < end:
        if hi < end and (lo == start or fence[lo - 1] < fence[hi + 1]):
            hi += 1
            height = min(height, fence[hi])
        else:
            lo -= 1
            height = min(height, fence[lo])
        res = max(res, height * (hi-lo+1))
    return res



t = int(input())
for _ in range(t):
    n = int(stdin.readline()) # 판자 수
    fence = list(map(int, stdin.readline().split()))
    print(solve(0, n - 1))