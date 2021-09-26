# 플로이드
from sys import stdin
INF = int(1e9)


def printSolution():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print(0, end=" "),
            else:
                print(graph[i][j], end=" "),
        print()


def floydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    printSolution()


n = int(stdin.readline())
m = int(stdin.readline())

graph = []
for i in range(n):
    graph.append([INF for _ in range(n)])
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    u, v, w = map(int, stdin.readline().split()) # 시작도시, 도착도시, 이동하는데 걸리는 시간
    graph[u-1][v-1] = min(graph[u-1][v-1], w)

floydWarshall()