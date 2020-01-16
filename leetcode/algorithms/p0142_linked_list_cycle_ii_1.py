class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        mapping, current = set(), head

        while current is not None:
            if current.next is not None and current.next in mapping:
                return current.next
            else:
                mapping.add(current)

            current = current.next

        return None
