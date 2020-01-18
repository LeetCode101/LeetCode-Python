class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while slow and fast:
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next

            if fast and slow == fast:
                return True

        return False
