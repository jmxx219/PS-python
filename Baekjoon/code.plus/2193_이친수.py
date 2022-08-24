from sys import stdin


def solve(index, prev):
    if index == N:
        return 1
    elif index > N:
        return 0

    if memo[index][prev] != -1:
        return memo[index][prev]

    cnt = 0
    cnt += solve(index + 1, 0)
    if prev != 1:
        cnt += solve(index + 1, 1)

    memo[index][prev] = cnt
    return cnt


N = int(stdin.readline())
if N <= 2:
    print(1)
else:
    N -= 2
    memo = []
    for _ in range(N):
        memo.append([-1] * 2) # prev 정보: 0, 1
    print(solve(0, 0))