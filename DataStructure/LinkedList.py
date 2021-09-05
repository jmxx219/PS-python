class ListNode:
    # 인스턴스 메서드(instance method) 호출 방법
    # 1. 해당 클래스 안에서는 self.메서드명
    # 2. 클래스 밖에서는 객체.메서드명

    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, item=0, next_item=None):
            self.item = item
            self.next = next_item

    def is_empty(self) -> bool:
        return not self.head

    def clear(self) -> None:
        self.head = None

    def get_tail(self):
        if self.is_empty():
            return None
        tail = self.head
        while tail.next:
            tail = tail.next
        return tail

    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr.item

    def remove_node(self, prev, curr) -> None:
        prev.next = curr.next
        self.size -= 1

    def push_front(self, key: int) -> None:
        new_node = self.Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def push_back(self, key: int) -> None:
        if self.is_empty():
            self.push_front(key)
        else:
            new_node = self.Node(key)
            tail = self.get_tail()
            tail.next = new_node
            self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise Exception("IndexError")
        delNode = self.head
        self.head = self.head.next
        self.size -= 1
        return delNode.item

    def middle_of_the_list(self) -> None:
        dummy = self.Node(-1, self.head)
        fast = slow = dummy
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow.item

    def find(self, key) -> bool:
        curr = self.head
        while curr:
            if curr.item == key:
                return True
            curr = curr.next
        return False

    def remove_first(self, key: int) -> None:
        if self.is_empty():
            return
        dummy = self.Node(-1, self.head)
        prev, curr = dummy, self.head
        while curr:
            if curr.item == key:
                self.remove_node(prev, curr)
                self.head = dummy.next
                break
            prev = curr
            curr = curr.next

    def remove_all(self, key: int) -> None:
        if self.is_empty():
            return
        dummy = self.Node(-1, self.head)
        prev, curr = dummy, self.head
        while curr:
            if curr.item == key:
                self.remove_node(prev, curr)
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

    def reverse(self):
        if self.size <= 1:
            return
        rev, curr = None, self.head
        while curr:
            node = curr
            curr = curr.next
            node.next = rev
            rev = node
        self.head = rev

    def print_node(self):
        curr = self.head
        while curr:
            print(curr.item, end=" ")
            curr = curr.next
        print()


if __name__ == "__main__":
    list_node = ListNode()
    list_node.push_back(1)
    list_node.push_back(2)
    list_node.push_back(2)
    list_node.push_back(2)
    list_node.push_back(2)
    list_node.push_back(3)
    list_node.push_back(3)
    list_node.push_back(3)
    list_node.push_back(4)
    list_node.push_back(5)
    list_node.push_back(6)
    list_node.print_node()

    list_node.remove_first(2)
    list_node.print_node()

    list_node.remove_all(2)
    list_node.print_node()

    print(list_node.find(2))

    list_node.reverse()
    list_node.print_node()

    print(list_node.middle_of_the_list())
