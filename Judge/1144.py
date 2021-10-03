# 두 개의 테이블, 서로 다른 전구
from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    cnt = 0
    # res = bin(a ^ b)
    # for i in range(2, len(res)):
    #     if res[i] == '1': cnt += 1

    res = a ^ b
    for i in range(32):
        if res & 1 == 1: cnt += 1
        res >>= 1
    print(cnt)