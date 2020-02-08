class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1, current2 = l1, l2
        dummy = ListNode(-1)
        prev = dummy
        carry = 0

        while current1 or current2:
            sum = carry

            if current1:
                sum += current1.val
                current1 = current1.next

            if current2:
                sum += current2.val
                current2 = current2.next

            carry = sum // 10
            prev.next = ListNode(sum % 10)
            prev = prev.next

        if carry != 0:
            prev.next = ListNode(carry)

        return dummy.next
