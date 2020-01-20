class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        step = 0
        dummy = ListNode(-1)
        dummy.next = head
        prev, current = dummy, head

        while current.next:
            if step >= n - 1:
                prev = prev.next

            step += 1
            current = current.next

        prev.next = prev.next.next

        return dummy.next
