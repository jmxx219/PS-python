class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        curr: ListNode = head
        prev: ListNode = None

        while head:
            curr = curr.next
            head.next = prev
            prev = head
            head = curr

        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        def reverse(curr: ListNode, prev: ListNode = None):
            if not curr:
                return prev
            next, curr.next = curr.next, prev
            return reverse(next, curr)

        return reverse(head)

    def reverseList3(self, head: ListNode) -> ListNode:
        curr, prev = head, None

        while curr:
            curr, head.next = curr.next, prev
            prev, head = head, curr

        return prev


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    curr = t.reverseList(head)
    while curr:
        print(curr.val, end=" ")
        curr = curr.next


