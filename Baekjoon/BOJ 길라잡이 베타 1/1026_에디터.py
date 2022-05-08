from sys import stdin


def solve():
    A.sort(reverse=True)
    B.sort()
    res = 0
    for i in range(N):
        res += A[i] * B[i]
    return res


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
print(solve())