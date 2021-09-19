from sys import stdin


def permute(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(N):
        res.append(i + 1)
        permute(depth + 1)
        res.pop()


N, M = map(int, stdin.readline().split())
visited = [False] * N
res = []
permute(0)

