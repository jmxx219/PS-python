class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0
        pass

    def enQueue(self, value: int) -> bool: # 요소 삽입
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
        else: # 꽉찬 상태
            return False

    def deQueue(self) -> bool: # 요소 삭제
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int: # 앞 항목 반환, 없으면 -1
        if self.q[self.front] is None:
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int: # 마지막 항목, 엉ㅄ으면 -1
        if self.q[self.rear - 1] is None:
            return -1
        else:
            return self.q[self.rear -1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None


if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(1) # return True
    myCircularQueue.enQueue(2) # return True
    myCircularQueue.enQueue(3) # return True
    myCircularQueue.enQueue(4) # return False
    myCircularQueue.Rear() # return 3
    myCircularQueue.isFull() # return True
    myCircularQueue.deQueue() # return True
    myCircularQueue.enQueue(4) # return True
    myCircularQueue.Rear() # return 4


