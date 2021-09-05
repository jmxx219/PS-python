from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
            nums_map[num] = i


if __name__ == "__main__":
    t = Solution()
    nums = [1, 2, 3, 4, 5, 7]
    target = 12
    print(t.twoSum2(nums, target))