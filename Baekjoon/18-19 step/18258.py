import sys
from collections import deque

N = int(input())
dq = deque()
for i in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push":
        dq.append(int(tmp[1]))
    elif tmp[0] == "pop":
        print(dq.popleft() if dq else -1)
    elif tmp[0] == "size":
        print(len(dq))
    elif tmp[0] == "empty":
        print(1 if not dq else 0)
    elif tmp[0] == "front":
        print(dq[0] if dq else -1)
    elif tmp[0] == "back":
        print(dq[-1] if dq else -1)
