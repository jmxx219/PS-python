import collections
import heapq
import sys
from sys import stdin


def dijkstra():
    dist = { node: sys.maxsize for node in graph }
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

    for node in d:
        if dist[node] == sys.maxsize:
            print(-1, end=" ")
        else:
            print(dist[node], end=" ")
    print()


def dijkstra2():
    Q = [(0, S)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    for node in d:
        if not dist[node]:
            print(-1, end=" ")
        else:
            print(dist[node], end=" ")
    print()


t = int(input())
for _ in range(t):
    graph = collections.defaultdict(list)
    tmp = list(map(int, stdin.readline().split())) # 노드, 간선, 출발 노드, 목적 노드 수
    N, E, S, K = tmp[:4]
    d = tmp[4:]

    tmp = list(map(int, input().split()))

    # for i in range(N): # dijkstra() 할 때 초기화
    #     graph[i] = []

    for x in range(0, len(tmp), 3):  # 출발, 도착, 소요 시간
        graph[tmp[x]].append((tmp[x+1], tmp[x+2]))
    dijkstra2()