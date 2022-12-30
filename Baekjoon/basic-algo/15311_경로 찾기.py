from sys import stdin


def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1
                # graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

    printSolution()


def printSolution():
    for row in graph:
        for col in row:
            print(col, end=" ")
        print()


N = int(stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, stdin.readline().split())))
floydWarshall()