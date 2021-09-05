class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0

        ten = 1
        while l1:
            num1 += l1.val * ten
            l1 = l1.next
            ten *= 10

        ten = 1
        while l2:
            num2 +=l2.val * ten
            l2 = l2.next
            ten *= 10

        res_num = num1 + num2
        if res_num == 0:
            return ListNode(0, None)

        res = ListNode(0, None)
        curr = res
        while res_num != 0:
            tmp = ListNode(res_num % 10, None)
            curr.next = tmp
            curr = curr.next
            res_num //= 10

        return res.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


if __name__ == "__main__":
    t = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    output = t.addTwoNumbers(l1, l2)
    while output:
        print(output.val, end=" ")
        output = output.next