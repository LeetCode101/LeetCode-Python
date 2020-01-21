class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.val < x:
            prev = prev.next

        current = prev

        while current and current.next:
            if current.next.val < x:
                next = current.next
                current.next = next.next
                next.next, prev.next = prev.next, next
                prev = prev.next
            else:
                current = current.next

        return dummy.next
