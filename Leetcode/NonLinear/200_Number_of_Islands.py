from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]

        def dfs(y, x):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
                return
            if grid[y][x] == "0":
                return

            grid[y][x] = "0"

            for i in range(4): # 동서남북 탐색
                dfs(y + dy[i], x + dx[i])

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt


if __name__ == "__main__":
    t = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(t.numIslands(grid))