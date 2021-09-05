from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        output = []

        def dfs():
            if len(output) == len(nums):
                res.append(output[:])
                return
            for n in nums:
                if n in output:
                    continue
                output.append(n)
                dfs()
                output.pop()

        dfs()
        return res


if __name__ == "__main__":
    t = Solution()
    nums = [1,2,3]
    print(t.permute(nums))