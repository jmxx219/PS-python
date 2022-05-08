# 0: 빈칸
from sys import stdin


def checkRow(x, a):
    for i in range(9):
        if a == board[x][i]:
            return False
    return True


def checkCol(y, a):
    for i in range(9):
        if a == board[i][y]:
            return False
    return True


def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return False
    return True


def dfs(idx: int):
    if idx == len(blank):
        return True

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            board[x][y] = i
            if dfs(idx + 1): return True
            board[x][y] = 0

    return False


def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.append((i, j))

    dfs(0)

    for i in range(9):
        print(*board[i])


board = []
blank = []

for _ in range(9):
    board.append(list(map(int, stdin.readline().rstrip().split())))

solve()


