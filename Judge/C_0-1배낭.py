# 0-1 배낭 채우기
from sys import stdin


class Item:
    def __init__(self, profit=0, weight=0):
        self.profit = profit
        self.weight = weight


def solve():
    A = []
    for _ in range(N + 1):
        A.append([0 for __ in range(W + 1)])

    for i in range(1, N + 1):
        for x in range(W + 1):
            if items[i].weight > x: A[i][x] = A[i-1][x]
            else: A[i][x] = max(A[i-1][x], A[i-1][x-items[i].weight] + items[i].profit)
    return A[N][W]


T = int(stdin.readline())
for _ in range(T):
    W, N = map(int, stdin.readline().split())
    tmp = list(map(int, stdin.readline().split()))
    items = [Item(0, 0)]
    for i in range(0, 2 * N, 2):
        items.append(Item(tmp[i], tmp[i+1]))
    print(solve())