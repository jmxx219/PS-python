import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums, reverse=True)
        return res[k-1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    t = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(t.findKthLargest2(nums, k))

