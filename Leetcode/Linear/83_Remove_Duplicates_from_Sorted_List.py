class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        prev, curr = head, head.next

        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = curr
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            head = self.deleteDuplicates2(head.next)
        else:
            head.next = self.deleteDuplicates2(head.next)

        return head


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    output = t.deleteDuplicates2(head)
    while output:
        print(output.val, end=" ")
        output = output.next