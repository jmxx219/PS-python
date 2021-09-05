import numbers
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, output):
            if i == len(digits):
                res.append(output)
                return
            for x in nums[digits[i]]:
                dfs(i + 1, output + x)

        if not digits:
            return []
        res = []
        output = ""
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        dfs(0, output)
        return res


if __name__ == "__main__":
    t = Solution()
    digits = ""
    print(t.letterCombinations(digits))