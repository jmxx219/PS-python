# 덱
from sys import stdin

N = int(stdin.readline())
queue = []

for i in range(N):
    func = list(map(str, stdin.readline().split()))
    if func[0] == "push_front":
        queue.insert(0, int(func[1]))
    elif func[0] == "push_back":
        queue.insert(len(queue), int(func[1]))
    elif func[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif func[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif func[0] == "size":
        print(len(queue))
    elif func[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif func[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
