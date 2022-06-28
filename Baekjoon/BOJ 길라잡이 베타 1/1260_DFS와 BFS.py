from sys import stdin


def dfs(v):
    visited2[v] = True
    print(v, end=" ")

    for i in range(1, N+1):
        if graph[v][i] and not visited2[i]:
            dfs(i)


def bfs():
    queue = [V]
    visited = [False for _ in range(N+1)]
    visited[V] = True

    while queue:
        here = queue.pop(0)
        print(here, end=" ")
        for i in range(1, N+1):
            if graph[here][i] and not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, stdin.readline().split()) # 정점 개수, 간선 개수, 시작 정점 번호
graph = []
for _ in range(N+1):
    graph.append([False for i in range(N+1)])

for i in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited2 = [False for _ in range(N+1)]
dfs(V)
print()
bfs()
