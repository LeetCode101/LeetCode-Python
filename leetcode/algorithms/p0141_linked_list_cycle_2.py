class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next if fast.next is None else fast.next.next

            if slow is not None and slow == fast:
                return True

        return False
