import sys


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def allWet(r1, r2):
    bl = [False for _ in range(n)]
    for i in range(n):
        if (points[i].x - ft1.x)**2 + (points[i].y - ft1.y)**2 <= r1:
            bl[i] = True
        if (points[i].x - ft2.x)**2 + (points[i].y - ft2.y)**2 <= r2:
            bl[i] = True

    for i in range(n):
        if not bl[i]:
            return False
    return True


def solve() -> int:
    res = sys.maxsize
    for i in range(n):
        for j in range(n):
            if allWet(dist1[i], dist2[j]):
                res = min(res, dist1[i] + dist2[j])

    return res


def distance(ft: Point, p: Point) -> int:
    a = p.x - ft.x
    b = p.y - ft.y
    return (a * a) + (b * b)


n, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

ft1 = Point(x1, y1) # 분수 좌표
ft2 = Point(x2, y2)
points = []
dist1 = []
dist2 = []

for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    p = Point(x, y)
    points.append(p)
    dist1.append(distance(ft1, p))
    dist2.append(distance(ft2, p))

print(solve())
