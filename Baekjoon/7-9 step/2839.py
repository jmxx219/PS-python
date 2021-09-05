target = int(input())
cnt = 0
while True:
    if (target % 5) == 0:
        cnt += (target // 5)
        print(cnt)
        break
    target -= 3
    cnt += 1
    if target < 0:
        print(-1)
        break