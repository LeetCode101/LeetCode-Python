class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1, current2 = self._reverse_list(l1), self._reverse_list(l2)
        prev = None
        carry = 0

        while current1 or current2:
            sum = carry

            if current1:
                sum += current1.val

            if current2:
                sum += current2.val

            carry = sum // 10
            new = ListNode(sum % 10)
            new.next, prev = prev, new

            if current1:
                current1 = current1.next

            if current2:
                current2 = current2.next

        if carry != 0:
            new = ListNode(carry)
            new.next, prev = prev, new

        return prev

    def _reverse_list(self, head: ListNode) -> ListNode:
        prev, current = None, head

        while current:
            next, current.next = current.next, prev
            prev, current = current, next

        return prev
