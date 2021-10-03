# 트리에서 갖아 먼 두 노드의 거리
import collections
from sys import stdin


def bfs(start):
    queue = collections.deque()
    dist = [-1 for _ in range(N + 1)]
    dist[start] = 0
    queue.append(start)

    while queue:
        here = queue.popleft()
        for v in graph[here]:
            if dist[v] == -1:
                dist[v] = dist[here] + 1
                queue.append(v)

    return max(dist), dist.index(max(dist))


T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    graph = collections.defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    dist, node = bfs(1)
    dist, node = bfs(node)
    print(dist)