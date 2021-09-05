import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x : int):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        return self.stack[-1] if self.stack else -1


if __name__ == "__main__":
    N = int(input())
    s = Stack()
    for i in range(N):
        tmp = sys.stdin.readline().split()
        if tmp[0] == "push":
            s.push(int(tmp[1]))
        elif tmp[0] == "pop":
            print(s.pop())
        elif tmp[0] == "size":
            print(s.size())
        elif tmp[0] == "empty":
            print(s.empty())
        elif tmp[0] == "top":
            print(s.top())