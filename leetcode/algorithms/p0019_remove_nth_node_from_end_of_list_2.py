class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        step = 0
        slow, fast = head, head

        while fast.next:
            if step >= n:
                slow = slow.next

            step += 1
            fast = fast.next

        if step == n - 1:
            return head.next
        else:
            slow.next = slow.next.next

            return head
