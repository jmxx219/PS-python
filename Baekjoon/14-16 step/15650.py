from sys import stdin


def permute(depth, index):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(index, N):
        res.append(i + 1)
        permute(depth + 1, i + 1)
        res.pop()


N, M = map(int, stdin.readline().split())
res = []
permute(0, 0)
