# 타임 머신
from sys import stdin
INF = int(1e9)


def BellmanFord(src):
    dist[src] = 0
    for i in range(N):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if i == N - 1:  # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False


N, M = map(int, stdin.readline().split()) # 도시, 버스 노선 개수
graph = []
dist = [INF] * (N + 1)
for _ in range(M):
    A, B, C = map(int, stdin.readline().split()) # 시작도시, 도착도시, 이동하는데 걸리는 시간
    graph.append([A, B, C])

if BellmanFord(1):
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] == INF:  # 도달할 수 없는 경우 -1 출력
            print('-1')
        else:  # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])