import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times: # 출발, 도착, 소요 시간
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                # 모든 노드 최단 경로 존재 여부 판별

        if len(dist) == N:
            return max(dist.values())
        return -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N + 1)}

        def dfs(node, cost):
            if cost >= dist[node]: return
            dist[node] = cost
            for time, nei in sorted(graph[node]):
                dfs(nei, cost + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


if __name__ == "__main__":
    t = Solution()
    times = [ # 출발, 도착, 소요 시간
        [0, 1, 1],
        [0, 2, 4],
        [1, 2, 2],
        [1, 3, 6],
        [2, 3, 3]
    ]
    n = 4 # 노드 갯수
    k = 0 # 출발 노드
    print(t.networkDelayTime(times, n, k))