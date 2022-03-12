def is_prime(num):
    if num == 1:
        return False

    for j in range(2, num + 1):
        if j*j <= num and num % j == 0:
            return False

    return True


if __name__ == '__main__':
    start = int(input())
    end = int(input())
    sum_s = 0
    min_prime = 0
    bl = False
    for i in range(start, end + 1):
        if is_prime(i):
            if not bl:
                min_prime = i
                bl = True
            sum_s += i
    if sum_s == 0:
        print(-1)
    else:
        print(sum_s)
        print(min_prime)