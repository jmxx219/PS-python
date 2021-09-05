nums = []
for i in range(10):
    x = int(input()) % 42
    nums.append(x)
num_set = set(nums)
print(len(num_set))
