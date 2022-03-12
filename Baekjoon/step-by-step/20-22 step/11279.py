# 최대힙
from sys import stdin
import heapq

n = int(stdin.readline())
heap = []
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -x)