# 통과 X
# XOR은 즐거워?
from sys import stdin


def solve():
    for s, i, j in command:
        if s == 1:
            box[i] ^= j
        else:
            tmp = box[i]
            i += 1
            while i <= j:
                tmp ^= box[i]
                i += 1
            print(tmp)


T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline()) # 수열 크기
    box = list(map(int, stdin.readline().split()))
    M = int(stdin.readline()) # 명령어 수
    command = []
    for __ in range(M):
        command.append(list(map(int, stdin.readline().split())))
    solve()
