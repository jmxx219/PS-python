from sys import stdin


def solve():
    i = 1
    res = 0
    while res <= k:
        res = pow(5, i)
        i += 1
    return i - 2


T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    print(solve())