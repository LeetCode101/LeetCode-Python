from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while slow and fast:
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next

            if slow == fast:
                break

        if not fast:
            return None

        p1, p2 = head, fast

        while p1 != p2:
            p1, p2 = p1.next, p2.next

        return p1
