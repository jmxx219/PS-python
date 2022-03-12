T = int(input())

for i in range(T):
    num, strs = input().split()
    for j in range(len(strs)):
        print(strs[j] * int(num), end = '')
    print()