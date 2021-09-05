class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = 1
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    break
                cnt += 1
            res = max(res, cnt)
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        set_s = set()
        res = 0
        start = end = 0
        while end < len(s):
            if s[end] in set_s:
                set_s.remove(s[start])
                start += 1
            else:
                set_s.add(s[end])
                end += 1
                res = max(res, end - start)
        return res

    def lengthOfLongestSubstring3(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length


if __name__ == "__main__":
    t = Solution()
    s = "abcabcbb"
    print(t.lengthOfLongestSubstring2(s))