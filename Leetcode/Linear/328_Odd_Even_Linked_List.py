class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = t.oddEvenList(head)
    while output:
        print(output.val, end=" ")
        output = output.next