# 부분합
import sys
from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

length = sys.maxsize
i = j = 0
sums = 0
while True:
    if sums >= S:
        length = min(length, j - i)
        sums -= nums[i]
        i += 1
    else:
        if j >= N:
            break
        else:
            sums += nums[j]
            j += 1


if length == sys.maxsize:
   print(0)
else:
   print(length)