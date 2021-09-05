class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for char in jewels:
            res += stones.count(char)
        return res

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        dic = {}

        for char in stones:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        res = 0
        for char in jewels:
            if char in dic:
                res += dic[char]
        return res


if __name__ == "__main__":
    t = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(t.numJewelsInStones2(jewels, stones))