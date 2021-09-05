import sys


def quadtree(quad: str):
    global index
    index += 1
    if quad[index] == "b" or quad[index] == "w":
        return quad[index]
    upperLeft = quadtree(quad)
    upperRight = quadtree(quad)
    lowerLeft = quadtree(quad)
    lowerRight = quadtree(quad)
    return "x" + lowerLeft + lowerRight + upperLeft + upperRight


t = int(input())
for _ in range(t):
    index = -1
    print(quadtree(sys.stdin.readline()))
