# 등산하기 어려운 산봉우리
import collections
import heapq
from math import inf
from sys import stdin


def solve():
    queue = []
    for m in mount:
        dist[m] = 0
        heapq.heappush(queue, (0, m))

    while queue:
        cost, here = heapq.heappop(queue)
        if dist[here] < cost:
            continue
        for v, w in graph[here]:
            nextDist = cost + w
            if nextDist < dist[v]:
                dist[v] = nextDist
                heapq.heappush(queue, (dist[v], v))


T = int(stdin.readline())
for _ in range(T):
    graph = collections.defaultdict(list)
    P, Q, R = map(int, stdin.readline().split()) # 산봉우리, 등산로, 산장 수

    for __ in range(Q):
        u, v, w = map(int, stdin.readline().split())
        graph[v].append([u, w])
    dist = [inf for _ in range(P + 1)]
    mount = list(map(int, stdin.readline().split()))

    solve()
    node = res = 0
    for i in range(1, P + 1):
        if res < dist[i]:
            res = dist[i]
            node = i
    print(node, res)