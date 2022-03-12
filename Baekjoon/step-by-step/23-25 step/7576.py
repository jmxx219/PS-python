# 토마토
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
from collections import deque
from sys import stdin


class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def print_box():
    for i in range(n):
        for j in range(m):
            print(box[i][j], end=" ")
        print()
    print()


def isRange(y, x):
    return 0 <= x < m and 0 <= y < n


def all():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False
    return True


def solve():
    day = 0
    queue = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append(Point(i, j))

    while queue:
        here = queue.popleft()
        for i in range(4):
            nextX = here.x + dx[i]
            nextY = here.y + dy[i]
            if isRange(nextY, nextX) and box[nextY][nextX] == 0:
                box[nextY][nextX] = box[here.y][here.x] + 1
                queue.append(Point(nextY, nextX))
                day = max(day, box[nextY][nextX])

    return day - 1 if all() else -1


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, stdin.readline().split())
box = []
for i in range(n):
    box.append(list(map(int, stdin.readline().split())))

if all():
    print(0)
else:
    print(solve())
