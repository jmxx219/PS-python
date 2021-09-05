import sys

t = int(input())
nums = []
op = []
i = 1
tmp = True
for _ in range(t):
    n = int(sys.stdin.readline())
    while i <= n:
        op.append("+")
        nums.append(i)
        i += 1
    if nums[-1] == n:
        nums.pop()
        op.append("-")
    else:
        tmp = False

if not tmp:
    print("NO")
else:
    for x in op:
        print(x)