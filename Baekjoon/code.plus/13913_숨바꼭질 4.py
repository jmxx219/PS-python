from sys import stdin


def solve():
    queue = [[N, 0]]
    discovered = [False] * 100001
    prevList = [-1] * 100001

    while queue:
        v, dist = queue.pop(0)

        if v == K:
            res = []
            prev = K
            while prev != N:
                res.append(prev)
                prev = prevList[prev]
            res.append(N)
            print(dist)
            for i in range(dist, -1, -1):
                print(res[i], end=' ')
            return

        next = [v - 1, v + 1, v * 2]
        for w in next:
            if w < 0 or w > 100000:
                continue

            if not discovered[w]:
                discovered[w] = True
                queue.append([w, dist + 1])
                prevList[w] = v


N, K = map(int, stdin.readline().split())
solve()