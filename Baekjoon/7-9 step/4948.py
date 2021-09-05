def sol(num):
    m = num + 1
    n = num * 2
    list_num = [i for i in range(2, n + 1)]

    for i in range(0, n - 1):
        if list_num[i] == 0:
            continue

        for j in range(i + list_num[i], n - 1, list_num[i]):
            list_num[j] = 0
    cnt = 0
    if m == 1:
        m += 1
    for i in range(m - 2, n - 1):
        if list_num[i] != 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    list_n = []
    while True:
        n = int(input())
        if n == 0:
            break
        print(sol(n))
