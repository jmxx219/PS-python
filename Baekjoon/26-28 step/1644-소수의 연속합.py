# 소수의 연속합 - 투 포인터


def countSum():
    res, start, end = 0, 0, 0

    while end <= len(nums):
        nums_sum = sum(nums[start:end])
        if nums_sum == N:
            res += 1
            end += 1
        elif nums_sum < N: end += 1
        else: start += 1

    return res


def prime_list(n): # 에라토스테네스 체
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i] == True]


N = int(input())
nums = prime_list(N)
# print(nums)
print(countSum())