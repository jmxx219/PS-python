import collections
import heapq
from sys import stdin

INF = 987654321


def solve():
    min_heap = [(0, 0)]
    visited = [False] * len(graph)
    keys = [INF] * len(graph)
    parent = [-1] * len(graph)
    total = 0

    while min_heap:
        dist, curr = heapq.heappop(min_heap)
        if visited[curr]:
            continue
        visited[curr] = True
        total += dist
        for v, w in graph[curr]:
            if not visited[v] and w < keys[v]:
                keys[v] = w
                parent[v] = curr
                heapq.heappush(min_heap, [w, v])

    # print(keys)
    # print(parent)
    return sum(keys[1:])


T = int(stdin.readline())
for _ in range(T):
    N, E = map(int, stdin.readline().split())
    graph = collections.defaultdict(list)
    tmp = list(map(int, stdin.readline().split()))
    for i in range(0, len(tmp), 3):
        graph[tmp[i]].append([tmp[i+1], tmp[i+2]])
        graph[tmp[i+1]].append([tmp[i], tmp[i+2]])
    print(solve())
