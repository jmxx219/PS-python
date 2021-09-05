class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.size, self.len = k, 0
        self.head.next, self.tail.prev = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        curr = node.next
        node.next = new
        new.prev, new.next = node, curr
        curr.prev = new

    def _del(self, node: ListNode):
        curr = node.next.next
        node.next = curr
        curr.prev = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.size:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.size:
            return False
        self.len += 1
        self._add(self.tail.prev, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.prev.prev)
        return True

    def getFront(self) -> int:
        return self.head.next.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.prev.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.size


if __name__ == "__main__":
    myCircularDeque = MyCircularDeque(3)
    myCircularDeque.insertLast(1) # return True
    myCircularDeque.insertLast(2) # return True
    myCircularDeque.insertFront(3) # return True
    myCircularDeque.insertFront(4) # return False, thequeue is full.
    myCircularDeque.getRear() # return 2
    myCircularDeque.isFull() # return True
    myCircularDeque.deleteLast() # return True
    myCircularDeque.insertFront(4) # return True
    myCircularDeque.getFront() # return 4