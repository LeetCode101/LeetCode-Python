class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        step = 0
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, head

        while fast.next:
            if step >= n - 1:
                slow = slow.next

            step += 1
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
