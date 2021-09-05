import math
import sys


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def solve() -> int:
    min_r1 = 0
    min_r2 = 0
    dist_f1_f2 = distance(ft1, ft2)
    for i in range(n):
        if c1_dist[i] <= min_r1 or c2_dist[i] <= min_r2:
            continue
        else:
            if c1_dist[i]**2 + min_r2**2 < c2_dist[i]**2 + min_r1**2:
                min_r1 = c1_dist[i]
            else:
                min_r2 = c2_dist[i]
        if min_r2 > dist_f1_f2 + min_r1:
            min_r1 = 0
        elif min_r1 > dist_f1_f2 + min_r2:
            min_r2 = 0
    return round((min_r1 ** 2 + min_r2 ** 2))


def distance(ft: Point, p: Point) -> int:
    a = p.x - ft.x
    b = p.y - ft.y
    return math.sqrt((a * a) + (b * b))


n, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

ft1 = Point(x1, y1)  # 분수 좌표
ft2 = Point(x2, y2)
points = []
c1_dist = []
c2_dist = []

for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    p = Point(x, y)
    points.append(p)
    c1_dist.append(distance(ft1, p))
    c2_dist.append(distance(ft2, p))

print(solve())