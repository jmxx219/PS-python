class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = 1
        curr = head
        while curr.next:
            cnt += 1
            curr = curr.next

        if cnt == n:
            return head.next

        curr = head
        for _ in range(cnt - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2))
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    output = t.removeNthFromEnd(head, n)
    while output:
        print(output.val, end=" ")
        output = output.next
