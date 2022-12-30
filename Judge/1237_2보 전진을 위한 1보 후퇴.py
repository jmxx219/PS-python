from sys import stdin

INF = 987654321
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def isRange(y, x):
    return 0 <= y < N and 0 <= x < N


def solve():
    if board[N-1][N-1] == 0 or board[0][0] == 0:
        return -1

    dists = [[INF] * N for _ in range(N)]
    discovered = [[False] * N for _ in range(N)]

    queue = [[0, 0, 0]]
    dists[0][0] = 0
    discovered[0][0] = True

    while queue:
        y, x, hereDist = queue.pop(0)
        for i in range(4):
            nextY = y + dy[i]
            nextX = x + dx[i]
            if isRange(nextY, nextX) and board[nextY][nextX] == 1 and not discovered[nextY][nextX]:
                for j in range(4):
                    nny = dy[j] + nextY
                    nnx = dx[j] + nextX
                    if nny == N - 1 and nnx == N - 1 and board[N-1][N-1] == 1:
                        return hereDist + 2

                discovered[nextY][nextX] = True
                dists[nextY][nextX] = hereDist + 3
                queue.append([nextY, nextX, dists[nextY][nextX]])
    return -1


N = int(stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))
print(solve())