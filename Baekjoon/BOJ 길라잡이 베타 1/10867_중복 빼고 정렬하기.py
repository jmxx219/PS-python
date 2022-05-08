from sys import stdin

N = int(stdin.readline())

nums = list(set(map(int, stdin.readline().split())))
nums.sort()
for i in nums:
    print(i, end=" ")