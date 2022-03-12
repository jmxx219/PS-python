# 미확인 도착지
import collections
import heapq
import sys
from sys import stdin


def dijkstra(S):
    dist = {node: sys.maxsize for node in range(1, n+1)}
    dist[S] = 0

    queue = []
    heapq.heappush(queue, (dist[S], S))

    while queue:
        cost, here = heapq.heappop(queue)

        if dist[here] < cost:
            continue

        for v, w in graph[here]:
            nextDist = cost + w
            if nextDist < dist[v]:
                dist[v] = nextDist
                heapq.heappush(queue, (nextDist, v))

    return dist


T = int(stdin.readline())

for _ in range(T):
    n, m, t = map(int, stdin.readline().split()) # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, stdin.readline().split()) # 출발지

    graph = collections.defaultdict(list)
    destination = []
    for __ in range(m):
        u, v, w = map(int, stdin.readline().split())
        graph[u].append([v, w])
        graph[v].append([u, w])
    for __ in range(t):
        destination.append(int(stdin.readline()))
    destination.sort()

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    for i in destination:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            print(i)