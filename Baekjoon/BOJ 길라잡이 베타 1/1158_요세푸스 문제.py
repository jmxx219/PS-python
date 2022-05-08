from collections import deque
from sys import stdin


def solve():
    arr = [i for i in range(1, N + 1)]
    res = []
    num = 0

    for i in range(N):
        num += K - 1
        if num >= len(arr):
            num %= len(arr)
        res.append(str(arr.pop(num)))

    print("<", ", ".join(res), ">", sep="")


def solve2():
    res = []
    queue = deque()

    for i in range(1, N+1):
        queue.append(i)

    while queue:
        for i in range(K-1):
            queue.append(queue.popleft())
        res.append(str(queue.popleft()))

    print("<", ", ".join(res), ">", sep="")


N, K = map(int, stdin.readline().split())
solve2()