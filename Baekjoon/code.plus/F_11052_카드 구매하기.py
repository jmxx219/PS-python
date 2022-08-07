from sys import stdin


def solve(card, sums): # 완전 탐색(전체 최대합 반환) -> 시간 초과
    if card == 0:
        return sums
    elif card < 0:
        return -INF

    ret = 0
    for i in range(N):
        ret = max(ret, solve(card - (i+1), sums + money[i]))

    return ret


def solve2(card): # 동적 -> 남은 카드의 개수가 card일 때, 해당 card 돈의 최댓값 반환(부분 최대합 반환)
    if card == 0:
        return 0
    elif card < 0:
        return -INF

    if memo[card] != -1:
        return memo[card]

    ret = 0
    for i in range(N):
        ret = max(ret, solve2(card - (i+1)) + money[i])

    memo[card] = ret
    return ret


INF = 987654321
N = int(stdin.readline())
money = list(map(int, stdin.readline().split()))
memo = [-1] * (N+1)
# print(solve(N, 0))
print(solve2(N))