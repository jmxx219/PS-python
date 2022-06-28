import math
from sys import stdin


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    dis = []
    for i in range(1, N):
        dis.append(trees[i] - trees[i-1])

    arr_gcd = math.inf
    for i in range(1, len(dis)):
        arr_gcd = min(arr_gcd, gcd(dis[i], dis[i-1]))

    res = 0
    for x in dis:
        res += (x // arr_gcd - 1)

    return res


N = int(stdin.readline())
trees = []
for i in range(N):
    trees.append(int(stdin.readline()))
print(solve())