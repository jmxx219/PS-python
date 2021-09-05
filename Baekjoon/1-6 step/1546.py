a = int(input())

nums = list(map(int, input().split()))
max_score = max(nums)

sum = 0
for i in range(a):
    sum += nums[i] / max_score * 100
print(sum/a)