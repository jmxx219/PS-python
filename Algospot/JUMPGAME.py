from sys import stdin


def solve(y: int, x: int):
    if y >= n or x >= n:
        return 0

    if y == n-1 and x == n-1:
        return 1

    if cache[y][x] != -1:
        return cache[y][x]

    cache[y][x] = solve(y + board[y][x], x) or solve(y, x + board[y][x])
    return cache[y][x]


c = int(input())
for _ in range(c):
    n = int(stdin.readline())
    board = []
    for i in range(n):
        board.append(list(map(int, stdin.readline().split())))
    cache = [[-1] * n for _ in range(n)]
    if solve(0, 0) == 1:
        print("YES")
    else:
        print("NO")