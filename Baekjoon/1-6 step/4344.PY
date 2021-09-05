x = int(input())
for i in range(x):
    stu = list(map(int, input().split()))
    avg = 0
    for j in range(stu[0]):
        avg += stu[j+1]
    avg /= stu[0]
    cnt = 0
    for j in range(stu[0]):
        if stu[j+1] > avg:
            cnt += 1
    print("{:.3f}%".format(cnt / stu[0] * 100))
    