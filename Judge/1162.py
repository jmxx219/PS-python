# 통과 x
# 쉬운 수학, 어려운 프로그래밍
from sys import stdin


def solve(n):
    table = [1, 2, 3]

    i = 0
    for _ in range(n - 3):
        table[i] = table[(i) % 3] + table[(i + 1) % 3] + table[(i + 2) % 3]
        i = (i + 1) % 3

    return ( table[(i - 1) % 3] if n > 3 else table[n - 1] ) % 1000000007


def solve2(n):
    if n <= 3:
        return n

    first = 1
    second = 2
    third = 3
    for i in range(n - 3):
        curr = first + second + third
        first = second
        second = third
        third = curr

    return curr % 1000000007


T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    print(solve2(n))