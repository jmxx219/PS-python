from sys import stdin


def permute(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            res.append(i + 1)
            permute(depth + 1)
            visited[i] = False
            res.pop()


def permute2():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(N):
        if i in res:
            continue
        res.append(i)
        permute()
        res.pop()


N, M = map(int, stdin.readline().split())
visited = [False] * N
res = []
# permute(0)
permute2(0)

