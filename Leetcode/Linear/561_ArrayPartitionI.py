from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    t = Solution()
    nums = [1,4,3,2]
    print(t.arrayPairSum(nums))