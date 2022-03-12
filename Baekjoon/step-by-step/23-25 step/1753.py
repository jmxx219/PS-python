# 최단경로
import collections
import heapq
import sys
from sys import stdin


def dijkstra():
    dist = {node: sys.maxsize for node in range(1, V+1)}
    dist[K] = 0

    queue = []
    heapq.heappush(queue, (dist[K], K))

    while queue:
        cost, here = heapq.heappop(queue)

        if dist[here] < cost:
            continue

        for v, w in graph[here]:
            nextDist = cost + w
            if nextDist < dist[v]:
                dist[v] = nextDist
                heapq.heappush(queue, (nextDist, v))

    for node in range(1, V + 1):
        if dist[node] == sys.maxsize:
            print("INF")
        else:
            print(dist[node])


V, E = map(int, stdin.readline().split()) # 정점 개수, 간선 개수
K = int(stdin.readline()) # 시작 정점 번호

graph = collections.defaultdict(list)

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])
dijkstra()

