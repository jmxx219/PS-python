# 이분 그래프
from collections import defaultdict, deque
from sys import stdin


def bfs(start):
    queue = deque()
    queue.append(start)
    colored[start] = 1 # 0: 방문 x, 1: 빨강, -1: 파랑

    while queue:
        here = queue.popleft()
        for next_v in graph[here]:
            if colored[next_v] == 0:
                colored[next_v] = -colored[here]  # here과 인접한 노드는 반대의 색으로
                queue.append(next_v)
            elif colored[here] == colored[next_v]:
                return False
    return True


k = int(stdin.readline())
for _ in range(k):
    graph = defaultdict(list)
    V, E = map(int, stdin.readline().split())

    for __ in range(E):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    bl = True
    colored = [0] * (V + 1)
    for node in range(1, V + 1):    # 연결: 한 번 탐색, 비연결: 모든 정점 탐색
        if colored[node] == 0 and not bfs(node):   # 하나의 정점에서라도 이분 그래프가 되지 않으면 NO
            bl = False
            break
    print("YES" if bl else "NO")