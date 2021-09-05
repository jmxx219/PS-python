class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2](leftmost is front of the queue)
    myQueue.push(3)
    print(myQueue.pop()) # return 1
    print(myQueue.pop())  # return 2
    print(myQueue.pop())  # return 3
    myQueue.push(4)
    print(myQueue.pop())  # return 4
    print(myQueue.empty()) # return false
