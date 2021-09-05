from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        s.reverse()


if __name__ == "__main__":
    t = Solution()
    s = ["H","a","n","n","a","h"]
    t.reverseString(s)
    print(s)