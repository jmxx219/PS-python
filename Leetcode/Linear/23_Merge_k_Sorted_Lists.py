import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        sorted_list = []
        for li in lists:
            while li:
                sorted_list.append(li.val)
                li = li.next
        sorted_list = sorted(sorted_list)

        dummy = cur = ListNode()
        for i in sorted_list:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    t = Solution()
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    output = t.mergeKLists(lists)
    while output:
        print(output.val, end=" ")
        output = output.next
