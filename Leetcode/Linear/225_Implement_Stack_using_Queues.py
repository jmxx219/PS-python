import collections


class MyStack:

    def __init__(self):
        self.dq = collections.deque()

    def push(self, x: int) -> None:
        self.dq.append(x)
        for _ in range(len(self.dq)-1):
            self.dq.append(self.dq.popleft())

    def pop(self) -> int:
        return self.dq.popleft()

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0


if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())  # return 2
    print(myStack.pop())  # return 2
    print(myStack.empty())  # return False
