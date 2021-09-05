x = int(input())
tmp = x
cnt = 0

while True:
    tmp = tmp % 10 * 10 + (tmp // 10 + tmp % 10) % 10
    cnt += 1
    if(tmp == x):
        break
print(cnt)
