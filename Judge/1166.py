# 나머지
from sys import stdin


T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    print(a % b)