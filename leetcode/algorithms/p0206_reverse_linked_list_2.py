class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverse(None, head)

    def _reverse(self, prev, current):
        if not current:
            return prev

        next, current.next = current.next, prev

        return self._reverse(current, next)
