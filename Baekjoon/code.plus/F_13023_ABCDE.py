from collections import defaultdict
from sys import stdin


def dfs(v, depth):
    if depth == 4:
        return True

    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            if dfs(w, depth + 1):
                return True
            visited[w] = False
    return False


def solve():
    for i in range(N):
        visited[i] = True
        if dfs(i, 0):
            print(1)
            return
        visited[i] = False

    print(0)


N, M = map(int, stdin.readline().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
solve()