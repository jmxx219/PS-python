import re


class Solution(object):
    def isPalindrome(self, s):
        # st = "".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        st = re.sub('[^a-z0-9]', '', s.lower())
        return st == st[::-1]


if __name__ == "__main__":
    t = Solution()
    print(t.isPalindrome("A man, a plan, a canal: Panama"))
