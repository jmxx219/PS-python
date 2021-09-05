from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        output = []

        def dfs(x : int):
            if len(output) == k:
                res.append(output.copy())
                return

            for i in range(x, n + 1):
                output.append(i)
                dfs(i + 1)
                output.pop()
                pass

        dfs(1)
        return res


if __name__ == "__main__":
    t = Solution()
    n = 1
    k = 1
    print(t.combine(n, k))