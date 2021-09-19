# 나무 자르기

from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().strip().split()))

lo = 0
hi = max(trees)
while lo <= hi:
    mid = (lo + hi) // 2
    meter = sum(x - mid if x - mid > 0 else 0 for x in trees)
    # for x in trees:
    #     if x > mid:
    #         meter += x - mid

    if meter < M:
        hi = mid - 1
    elif meter >= M:
        lo = mid + 1
print(hi)
