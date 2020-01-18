class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev, current = dummy, dummy.next

        while current and current.next:
            next = current.next
            current.next, next.next, prev.next = next.next, current, next
            prev, current = current, current.next

        return dummy.next
