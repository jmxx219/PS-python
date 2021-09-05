from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [ 0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res


if __name__ == "__main__":
    t = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(t.dailyTemperatures(temperatures))