class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head

        while current:
            next, current.next = current.next, prev
            prev, current = current, next

        return prev
