from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow
