class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(0, head)
        for _ in range(left - 1):
            start = start.next

        prev, end = start.next, start.next.next
        for _ in range(right - left):
            prev.next = end.next
            end.next = start.next
            start.next = end
            end = prev.next

        return root.next

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(0, head)
        for _ in range(left - 1):
            start = start.next

        end = start.next
        for _ in range(right - left):
            prev = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = prev

        return root.next



if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left, right = 2, 4
    output = t.reverseBetween(head, left, right)
    while output:
        print(output.val, end=" ")
        output = output.next

