import sys

k = int(input())
nums = []
sum_n = 0
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0 and nums:
        sum_n -= nums.pop()
    else:
        nums.append(n)
        sum_n += n

print(sum_n)