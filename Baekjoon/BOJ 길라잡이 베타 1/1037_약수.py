from sys import stdin

N = int(stdin.readline()) # 약수 개수
nums = list(map(int, stdin.readline().split()))
print(max(nums) * min(nums))

