class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second

            first.next = second.next
            second.next = first
            prev = prev.next.next

        return dummy.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs2(p.next)
            p.next = head
            return p
        return head


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = t.swapPairs(head)
    while output:
        print(output.val, end=" ")
        output = output.next
