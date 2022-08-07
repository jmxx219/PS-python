from collections import defaultdict, Counter
from sys import stdin


def solve_F(): # 시간 초과
    F_A = Counter(nums)
    res = [-1] * N
    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if F_A[nums[i]] < F_A[nums[j]]:
                res[i] = nums[j]
                break
    print(*res)


def solve_S():
    F_A = Counter(nums)
    res = [-1] * N
    stack = [0]

    for i in range(1, N):
        while stack and F_A[nums[stack[-1]]] < F_A[nums[i]]:
            res[stack.pop()] = nums[i]
        stack.append(i)

    print(*res)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split(' ')))
solve_S()
