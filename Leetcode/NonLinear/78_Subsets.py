from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            res.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        res = []
        dfs(0, [])
        return res


if __name__ == "__main__":
    t = Solution()
    nums = [1,2,3]
    print(t.subsets(nums))