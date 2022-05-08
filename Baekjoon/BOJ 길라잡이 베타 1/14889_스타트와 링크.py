import itertools
import math
from sys import stdin
from typing import List


def score_sum(nCr: List[int]):
    nPr = list(itertools.permutations(nCr, 2))
    team_sum = 0

    for a, b in nPr:
        team_sum += (board[a-1][b-1])

    return team_sum


def solve():
    arr = [i for i in range(1, N + 1)]
    nCr = list(itertools.combinations(arr, N // 2))
    res = math.inf
    lo, hi = 0, len(nCr) - 1

    while lo < hi:
        start = score_sum(nCr[lo])
        link = score_sum(nCr[hi])
        res = min(res, abs(start - link))

        lo += 1
        hi -= 1

    return res


N = int(stdin.readline())   # 축구하기 위해 모인 사람(짝수)
board = []

for i in range(N):
    board.append(list(map(int, stdin.readline().split())))

print(solve())