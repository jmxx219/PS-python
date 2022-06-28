import math


def conversion_nTok(n, k):
    res = []

    while n > 0:
        share, remain = divmod(n, k)
        res.append(str(remain))
        n = share

    res.reverse()

    return ''.join(res)


def is_prime(num):
    if num <= 1: return False

    bl = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            bl = False

    return bl


def solution(n, k):
    res = 0
    nums = conversion_nTok(n, k).split('0')

    # print(nums)

    for x in nums:
        if x != '' and is_prime(int(x, base=10)):
            res += 1

    return res


print(solution(2, 5))
print(solution(437674, 3))
print(solution(110011, 10))