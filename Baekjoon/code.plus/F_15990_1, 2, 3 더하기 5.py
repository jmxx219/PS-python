import sys
from sys import stdin

sys.setrecursionlimit(10 ** 8)


# memo[] : 이전에 대한 정보가 2개이므로 최적 부분 구조 성립 x
# memo[][]: 변화는 값들(이전에 대한 정보)인 target과 prev를 2차원 배열로
def cntSumTarget(target, prev):
    if target == 0:
        return 1
    elif target < 0:
        return 0

    if memo[target][prev] != -1:
        return memo[target][prev]

    cnt = 0
    for i in range(1, 4):
        if i != prev:
            cnt = (cnt + cntSumTarget(target - i, i)) % MOD
    memo[target][prev] = cnt
    return cnt


MOD = 1000000009
memo = []
for __ in range(100000 + 1):
    memo.append([-1] * 4)

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    print(cntSumTarget(N, 0))