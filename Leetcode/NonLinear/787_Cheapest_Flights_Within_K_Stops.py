import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        vis = collections.defaultdict(int)

        for s, d, c in flights:
            graph[s] += [(c, d)]

        q = [(0, src, k + 1)]

        while q:
            tc, start, stops = heapq.heappop(q)

            if start == dst:
                return tc

            if vis[start] < stops:
                vis[start] = stops - 1
                for ct, nei in graph[start]:
                    heapq.heappush(q, (ct + tc, nei, vis[start]))

        return -1


if __name__ == "__main__":
    t = Solution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]  # from, to, price
    src = 0  # 시작점
    dst = 2  # 도착점
    k = 1  # 경유지 개수
    print(t.findCheapestPrice(n, flights, src, dst, k))
