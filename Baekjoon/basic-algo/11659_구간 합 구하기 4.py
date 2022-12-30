from sys import stdin


def solve():
    psum = [0] * (N+1)

    for i in range(1, N+1):
        psum[i] = psum[i-1] + nums[i-1]

    for i, j in ranges:
        print(psum[j] - psum[i-1])


N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
ranges = []
for _ in range(M):
    ranges.append(list(map(int, stdin.readline().split())))
solve()