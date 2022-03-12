# 이항 계수 3 - 분할 정복
# 참고: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11401-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-3-%EA%B3%A8%EB%93%9C1-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

from sys import stdin


def bino_coef_factorial(n) :
    ans = 1

    for i in range(2,  n+1):
        ans *= i

    return ans


def bino_coef_recursion(n, k):
    if k == 0 or k == n:
        return 1

    return bino_coef_recursion(n - 1, k) + bino_coef_recursion(n - 1, k - 1)


def bino_coef_dynamic_memo(n, k, memo):
    if memo[n][k] > 0 :
        return memo[n][k]

    if k == 0 or k == n:
        memo[n][k] = 1
        return 1

    memo[n][k] = bino_coef_dynamic_memo(n - 1, k, memo) + bino_coef_dynamic_memo(n - 1, k - 1, memo)

    return memo[n][k]


def bino_coef_dynamic_tabu(n, k):
    memo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(0, n + 1):
        for j in range(0, k + 1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j] + memo[i - 1][j - 1]

    return memo[n][k]


# 팩토리얼 계산(나머지 연산 적용)
def factorial(n, p) :
    ans = 1

    for i in range(2,  n+1):
        ans  = (ans * i) % p

    return ans


# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
    if k == 0:  return 1
    elif k == 1:    return n

    tmp = square(n, k // 2)
    if k % 2:   return tmp * tmp * n % p
    else:   return tmp * tmp % p


if __name__ == "__main__":
    N, K = map(int, stdin.readline().split())

    # 1. 팩토리얼
    res1 = bino_coef_factorial(N) // (bino_coef_factorial(N - K) * bino_coef_factorial(K))  # nCk = n!((n-k)! * k!)^(-1)

    # 2. 재귀 - 분할정복
    res2 = bino_coef_recursion(N, K) # nCk = n-1Ck + n-1Ck-1

    # 3. 동적 계획법 - 메모이제이션
    memo = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    res3 = bino_coef_dynamic_memo(N, K, memo)

    # 4. 동적 계획법 - 테뷸레이션
    res4 = bino_coef_dynamic_tabu(N, K)

    # 5. 페르마의 소정리 + 분할정복
    p = 1000000007
    top = factorial(N, p)
    bot = factorial(N - K) * factorial(K) % p
    res = top * square(bot, p-2) % p # nCk % p = n!((n−k)!k!)^(-1) % p = n!((n−k)!k!)^(p-2) % p

    print(res)
