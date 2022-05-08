from sys import stdin

N = int(stdin.readline())
points = []

for i in range(N):
    p = list(map(int, stdin.readline().split()))
    points.append(p)

points.sort(key=lambda x : (x[0], x[1]))
for point in points:
    print(point[0], point[1])
