a = int(input())
b = int(input())
c = int(input())

# target = a * b * c

# nums = [0 for _ in range(10)]
# while(target != 0): 
#     tmp = target % 10
#     nums[tmp] += 1
#     target //= 10


# for i in range(0, 10):
#     print(nums[i])

x = list(map(int, (str(a * b * c))))
for i in range(10):
    print(x.count(i))