# 랜선 자르기
from sys import stdin

K, N = map(int, stdin.readline().split())
nums = []
for _ in range(K):
    nums.append(int(stdin.readline()))

lo = 1
hi = max(nums)
while lo <= hi:
    mid = (lo + hi) // 2
    length = 0
    for x in nums:
        length += x // mid
    if length < N:
        hi = mid - 1
    elif length >= N:
        lo = mid + 1
print(hi)