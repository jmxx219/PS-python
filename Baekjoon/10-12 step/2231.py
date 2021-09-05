# 분해합

n = int(input())
res = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    res = i + sum(nums)
    if res == n:
        print(i)
        break
    if i == n:
        print(0)