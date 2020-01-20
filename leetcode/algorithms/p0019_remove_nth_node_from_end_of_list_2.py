class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        prev, current = head, head

        while current.next:
            size += 1
            current = current.next

            if size > n + 1:
                prev = prev.next

        if size == n:
            return head.next
        else:
            prev.next = prev.next.next

            return head
