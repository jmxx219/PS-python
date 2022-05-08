from sys import stdin
from typing import List


def solve(target: int):
    if target == 0:
        return 1
    elif target < 0:
        return 0

    cnt = 0

    for i in range(1, 4):
        cnt += solve(target - i)

    return cnt


def solve2(target: int, memo: List[int]):
    if target == 0:
        return 1
    elif target < 0:
        return 0

    if memo[target] != -1:
        return memo[target]

    cnt = 0

    for i in range(1, 4):
        cnt += solve(target - i)

    memo[target] = cnt

    return memo[target]


def solve3(N: int):
    table = [0 for i in range(N + 1)]
    table[0] = 1

    for i in range(N):
        if table[i] != 0:
            for x in range(1, 4):
                if i + x <= N:
                    table[i + x] += table[i]

    return table[N]


if __name__ == "__main__":
    T = int(stdin.readline())

    for i in range(T):
        N = int(stdin.readline())
        # print(solve(N))

        # memo = [-1 for i in range(N + 1)]
        # print(solve2(N, memo))

        print(solve3(N))