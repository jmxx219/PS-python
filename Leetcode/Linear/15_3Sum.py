from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너띄기기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵처리
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = list(counter.keys())

        ans = set()

        if counter[0] >= 3: ans.add((0, 0, 0))
        pos, neg = [x for x in nums if x > 0], [x for x in nums if x < 0]

        for a in neg:
            for b in pos:
                c = -(a + b)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    ans.add(tuple(sorted([a, b, c])))
        return ans


if __name__ == "__main__":
    t = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(t.threeSum(nums))
    print(t.threeSum2(nums))
