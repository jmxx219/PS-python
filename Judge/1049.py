# 이 회사의 순이익이 궁금해
import sys
from sys import stdin
INT_MAX = 2147483647


def solve():
    lo = 0
    hi = INT_MAX
    res = INT_MAX

    while lo <= hi:
        N = (lo + hi) // 2
        # print(lo, N, hi)
        tp = (N // 3) + (N // K) * 3
        if P == tp:
            if res > N: res = N
            hi = N - 1
        elif P < tp:
            hi = N - 1
        else:
            lo = N + 1

    print(res if res != INT_MAX else -1)


T = int(stdin.readline())
for _ in range(T):
    P, K = map(int, stdin.readline().split())
    solve()