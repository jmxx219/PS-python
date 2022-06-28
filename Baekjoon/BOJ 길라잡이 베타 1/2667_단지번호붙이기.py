# 1: 집 존재 o
# 0: 집 존재 x
from sys import stdin


def is_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def bfs(x, y):
    visited = set([x, y])
    board[x][y] = 0
    cnt = 1
    queue = [[x, y]]

    while queue:
        here_x, here_y = queue.pop(0)
        for i in range(4):
            next_x = here_x + next[i][0]
            next_y = here_y + next[i][1]
            if is_range(next_x, next_y) and board[next_x][next_y] == 1 and not (next_x, next_y) in visited:
                visited.add((next_x, next_y))
                queue.append([next_x, next_y])
                cnt += 1
                board[next_x][next_y] = 0

    return cnt


def solve():
    cnt = 0
    groups = []

    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                cnt += 1
                groups.append(bfs(x, y))

    print(cnt)
    groups.sort()
    for group in groups:
        print(group)


next = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, stdin.readline().rstrip())))
solve()
