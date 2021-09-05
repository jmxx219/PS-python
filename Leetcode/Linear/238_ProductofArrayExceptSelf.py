import copy
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        product = 1
        for i in range(0, len(nums)):
            out.append(product)
            product = product * nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * product
            product = product * nums[i]

        return out


if __name__ == "__main__":
    t = Solution()
    nums = [1, 2, 3, 4]
    print(t.productExceptSelf(nums))
