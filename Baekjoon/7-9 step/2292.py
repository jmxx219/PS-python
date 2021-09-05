x = int(input())
res = 0
tmp = 1
while x > tmp:
    tmp += res * 6
    res += 1
if res == 0:
    print(1)
else:
    print(res)