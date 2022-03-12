def is_prime(num):
    if num == 1:
        return False

    for j in range(2, num + 1):
        if j*j <= num and num % j == 0:
            return False

    return True


if __name__ == '__main__':
    n = int(input())
    list_n = list(map(int, input().split()))
    cnt = 0
    for i in range(len(list_n)):
        if is_prime(list_n[i]):
            cnt += 1
    print(cnt)