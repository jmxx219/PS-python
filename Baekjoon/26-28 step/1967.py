# 트리의 지름
import collections
import heapq
from sys import stdin
INF = int(1e9)


def dijkstra(S):
    queue = []
    dist = [INF for _ in range(n + 1)]

    dist[S] = 0
    heapq.heappush(queue, (dist[S], S))

    while queue:
        cost, here = heapq.heappop(queue)

        if dist[here] < cost:
            continue

        for v, w in graph[here]:
            nextDist = cost + w
            if nextDist < dist[v]:
                dist[v] = nextDist
                heapq.heappush(queue, (dist[v], v))

    return dist


n = int(stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

d_ = dijkstra(10) # 루트 정점(1번)을 기준으로 가장 가중치가 높은 정점을 찾는다.
print(max(dijkstra(d_.index(max(d_[1:])))[1:])) # 다시  그 정점을 기준으로 가중치가 가장 높은 것을 출력한다.
