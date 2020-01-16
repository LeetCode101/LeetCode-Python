class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next if fast.next is None else fast.next.next

            if fast is not None and slow == fast:
                break

        if fast is None:
            return None

        p1, p2 = head, fast

        while p1 != p2:
            p1, p2 = p1.next, p2.next

        return p1
