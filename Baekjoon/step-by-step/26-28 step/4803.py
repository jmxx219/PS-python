# 트리
import collections
from sys import stdin


def isCyclicUtil(v, visited, parent):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            if isCyclicUtil(i, visited, v):
                return True
        elif i != parent: # 이미 방문했고 해당 노드의 부모가 아니라면 주기가 있다.
            return True

    return False


def solve():
    visited = [False] * (n + 1)
    treeCnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        if not isCyclicUtil(i, visited, -1):
            treeCnt += 1

    if treeCnt == 0:
        print("No trees.")
    elif treeCnt == 1:
        print("There is one tree.")
    else:
        print(f'A forest of {treeCnt} trees.')


case = 1
while True:
    n, m = map(int, stdin.readline().split())  # 정점, 간선
    if n == 0 and m == 0:
        break
    graph = collections.defaultdict(list)
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(f'Case {case}:', end=" ")
    solve()
    case += 1
