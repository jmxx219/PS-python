from sys import stdin
from typing import List


def promising(row: int):
    flag = True
    r = 0

    while r < row and flag:
        if cols[r] == cols[row] or abs(cols[r] - cols[row]) == (row - r):  # 대각선이 있는지 검사
            flag = False
        r += 1

    return flag


# def nQueens(row: int): # 시간 초과
#     cnt = 0
#
#     for c in range(N):
#         cols[row] = c
#         if promising(row): # 유망한지 검사
#             if row + 1 == N:
#                 return 1
#             else:
#                 cnt += nQueens(row+1)
#
#     return cnt


def nQueens2(row: int):
    global cnt

    if row == N:
        cnt += 1
    else:
        for c in range(N):
            if visited[c]:
                continue
            cols[row] = c
            if promising(row):
                visited[c] = True
                nQueens2(row + 1)
                visited[c] = False


N = int(stdin.readline())
cols = [0 for i in range(N)]
visited = [False] * N
cnt = 0

nQueens2(0)
print(cnt)
