class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head

        return self.reverse(prev, current)

    def reverse(self, prev, current):
        if current is None:
            return prev

        next = current.next
        current.next = prev

        return self.reverse(current, next)
