# 트리의 지름 - 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
import collections
from sys import stdin


def bfs(start):
    dist = [-1] * (V + 1)
    queue = collections.deque()

    queue.append(start)
    dist[start] = 0
    max_d = [0, 0] # 시작노드에서 가장 먼 거리, 노드

    while queue:
        here = queue.popleft()
        for u, w in graph[here]:
            if dist[u] == -1:
                dist[u] = dist[here] + w
                queue.append(u)
                if max_d[0] < dist[u]:
                    max_d = dist[u], u

    return max_d


V = int(stdin.readline())
graph = collections.defaultdict(list)

for _ in range(V):
    tmp = list(map(int, stdin.readline().split()))
    for i in range(1, len(tmp) - 2, 2):
        graph[tmp[0]].append([tmp[i], tmp[i + 1]])

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
