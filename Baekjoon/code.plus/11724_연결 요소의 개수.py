import sys
from collections import defaultdict
from sys import stdin

sys.setrecursionlimit(100000)


def Connected(S, discovered):
    discovered[S] = True
    for w in graph[S]:
        if not discovered[w]:
            Connected(w, discovered)


def solve():
    discovered = [False] * N
    cnt = 0
    for i in range(N):
        if not discovered[i]:
            Connected(i, discovered)
            cnt += 1
    return cnt


N, M = map(int, stdin.readline().split()) # 정점, 간선 개수
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
print(solve())