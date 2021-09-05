lists = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
num = list(input())
res = 0
for i in range(len(num)):
    for j in range(len(lists)):
        if num[i] in lists[j]:
            res = res + j + 3
print(res)
