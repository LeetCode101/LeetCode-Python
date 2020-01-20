class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        prev, current = head, head

        while current:
            if size > n:
                prev = prev.next

            size += 1
            current = current.next

        if size == n:
            return head.next
        else:
            prev.next = prev.next.next

            return head
