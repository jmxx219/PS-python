# 수 찾기
from sys import stdin

n = int(stdin.readline())
ns = list(map(int, stdin.readline().split()))
ns = sorted(ns)

m = int(stdin.readline())
ms = list(map(int, stdin.readline().split()))

for x in ms:
    lo = 0
    hi = n - 1
    bl = False
    while lo <= hi:
        mid = (lo + hi) // 2
        if ns[mid] == x:
            bl = True
            break
        elif ns[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    print("1" if bl else "0")

