import sys
from sys import stdin

sys.setrecursionlimit(10000)

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]


def isRange(y, x):
    return 0 <= y < h and 0 <= x < w


def Connected(y, x):
    board[y][x] = 0
    for i in range(8):
        nextY = y + dy[i]
        nextX = x + dx[i]
        if isRange(nextY, nextX) and board[nextY][nextX] == 1:
            Connected(nextY, nextX)


def solve():
    cnt = 0
    for r in range(h):
        for c in range(w):
            if board[r][c] == 1:
                Connected(r, c)
                cnt += 1
    return cnt


while True:
    w, h = map(int, stdin.readline().split()) # 지도 너비, 높이
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, stdin.readline().split())))
    print(solve())
