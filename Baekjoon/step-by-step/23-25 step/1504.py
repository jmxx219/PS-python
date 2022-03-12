# 특정한 최단 경로
import collections
import heapq
import sys
from sys import stdin


def dijkstra(S):
    dist = {node: sys.maxsize for node in range(1, N+1)}
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


N, E = map(int, stdin.readline().split()) # 정점 개수, 간선 개수
graph = collections.defaultdict(list)

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
v1, v2 = map(int, stdin.readline().split()) # 반드시 거쳐야 하는 두 개의 서로 다른 정점

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

sol1 = original_distance[v1] + v1_distance[v2] + v2_distance[N]
sol2 = original_distance[v2] + v2_distance[v1] + v1_distance[N]

res = min(sol1, sol2)
if res >= sys.maxsize:
    print(-1)
else:
    print(min(sol1, sol2))
