# KoreaTech 세계 일주를 꿈꾸다!
from collections import deque
from sys import stdin


def solve():
    queue = deque()
    startC = 0
    sums = 0
    for i in range(2 * c):
        sums += oil_list[i]
        queue.append(oil_list[i])
        if i - startC + 1 == c and sums >= 0:
            break
        while sums < 0 and queue:
            sums -= queue.popleft()
            startC += 1

    if startC >= c:
        print(-1)
    else:
        print(startC)


T = int(stdin.readline())
for _ in range(T):
    c = int(stdin.readline())
    oil = list(map(int, stdin.readline().split()))
    fuel = list(map(int, stdin.readline().split()))

    oil_list = oil * 2
    for i in range(c):
        oil_list[i] = oil_list[i + c] = oil[i] - fuel[i]
    solve()