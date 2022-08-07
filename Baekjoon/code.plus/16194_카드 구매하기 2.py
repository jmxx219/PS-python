from sys import stdin


def solve(card):
    if card == 0:
        return 0
    elif card < 0:
        return INF

    if memo[card] != -1:
        return memo[card]

    ret = INF
    for i in range(N):
        ret = min(ret, solve(card - (i+1)) + money[i])

    memo[card] = ret

    return ret


INF = 987654321
N = int(stdin.readline())
money = list(map(int, stdin.readline().split()))
memo = [-1] * (N+1)
print(solve(N))