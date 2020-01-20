class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        step = 0
        prev, current = head, head

        while current.next:
            if step >= n:
                prev = prev.next

            step += 1
            current = current.next

        if step == n - 1:
            return head.next
        else:
            prev.next = prev.next.next

            return head
