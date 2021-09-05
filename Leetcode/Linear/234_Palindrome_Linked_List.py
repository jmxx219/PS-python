# Definition for singly-linked list.
import collections
from typing import List, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q : List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while slow:
            curr = curr.next
            slow.next = prev
            prev = slow
            slow = curr

        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next

        return True

    def isPalindrome4(self, head: ListNode) -> bool:
        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and slow and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev


if __name__ == "__main__":
    t = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(t.isPalindrome3(head))
