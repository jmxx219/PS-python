# 1로 만들기
import sys


def solve(n: int):  # top-down => 메모리 초과 발생
    if n == 1:
        return 0

    if memo[n] != - 1:
        return memo[n]

    a = solve(n // 3) if n % 3 == 0 else sys.maxsize
    b = solve(n // 2) if n % 2 == 0 else sys.maxsize
    c = solve(n - 1)

    memo[n] = min(a, b, c) + 1
    return memo[n]


def solve2(n: int): # bottom-up
    dp = [-1 for _ in range(x + 1)]
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        dp[i] = min(dp[i], dp[i // 3] + 1 if i % 3 == 0 else sys.maxsize)
        dp[i] = min(dp[i], dp[i // 2] + 1 if i % 2 == 0 else sys.maxsize)

    return dp[n]


def solve3(n: int):
    if n in memo:
        return memo[n]
        # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
        # 이 경우를 나머지로 더해주는 것으로 짐작된다.
    memo[n] = 1 + min(solve3(n // 2) + n % 2, solve3(n // 3) + n % 3)
    return memo[n]


x = int(sys.stdin.readline())

# 1
memo = [-1 for _ in range(x + 1)]
print(solve(x))

# 2
print(solve2(x))

# 3
memo = {1: 0, 2: 1}
print(solve3(x))