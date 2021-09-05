import sys
from sys import stdin

def print_m(y, x):
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            print(board[i][j],end="")
        print()

def isCount(y, x):
    first_W = 0  # W로 시작했을 때 칠해야 할 부분
    firstB = 0  # B로 시작했을 때 칠해야 할 부분
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (j + i) % 2 == 0:
                if board[i][j] != 'W': first_W += 1
                if board[i][j] != 'B': firstB += 1
            else:
                if board[i][j] != 'B': first_W += 1
                if board[i][j] != 'W': firstB += 1
    return min(first_W, firstB)


def solve():
    res = sys.maxsize
    for y in range(row - 7):
        for x in range(col - 7):
            res = min(res, isCount(y, x))
    return res


row, col = map(int, stdin.readline().split())
board = []
for x in range(row):
    board.append(list(stdin.readline().strip()))

print(solve())