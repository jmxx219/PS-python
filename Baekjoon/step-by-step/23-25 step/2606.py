# 바이러스
from collections import defaultdict
from sys import stdin

def solve():
    queue = []
    queue.append(1)
    visited = [False for _ in range(n + 1)]
    visited[1] = True
    cnt = 0
    while queue:
        here = queue.pop(0)
        for next in network[here]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                cnt += 1
    return cnt


n = int(stdin.readline())
pair = int(stdin.readline())
network = defaultdict(list)
for _ in range(pair):
    a, b = map(int, stdin.readline().split())
    network[a].append(b)
    network[b].append(a)
print(solve())