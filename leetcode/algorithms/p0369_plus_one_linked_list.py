class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        digits = []
        current = head

        while current:
            digits.append(current.val)
            current = current.next

        digits = self._plus_one(digits)
        dummy = ListNode(-1)
        prev = dummy

        for n in digits:
            current = ListNode(n)
            prev.next, prev = current, current

        return dummy.next

    def _plus_one(self, digits):
        if not digits:
            return []

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1

                return digits

            digits[i] = 0

        return [1] + digits
