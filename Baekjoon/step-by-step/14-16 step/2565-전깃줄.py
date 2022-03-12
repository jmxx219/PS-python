# 전깃줄 - 동적 계획법
from sys import stdin


def solve() :
    memo = [1] * N

    for i in range(N):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                memo[i] = max(memo[i], memo[j] + 1)


    return N - max(memo)


N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))
arr.sort()
print(solve())