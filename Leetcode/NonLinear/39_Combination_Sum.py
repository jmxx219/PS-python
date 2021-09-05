from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        output = []

        def dfs(index, t):
            if t < 0:
                return
            if t == 0:
                res.append(output.copy())
                return

            for i in range(index, len(candidates)):
                output.append(candidates[i])
                dfs(i, t - candidates[i])
                output.pop()

        dfs(0, target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


if __name__ == "__main__":
    t = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(t.combinationSum2(candidates, target))