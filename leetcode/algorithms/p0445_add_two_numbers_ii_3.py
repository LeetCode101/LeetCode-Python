class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self._get_list_sum(l1) + self._get_list_sum(l2)
        numbers = list(str(sum))
        dummy = ListNode(-1)
        prev = dummy

        for n in numbers:
            new = ListNode(int(n))
            prev.next, prev = new, new

        return dummy.next

    def _get_list_sum(self, head: ListNode) -> int:
        sum, current = 0, head

        while current:
            sum = sum * 10 + current.val
            current = current.next

        return sum
