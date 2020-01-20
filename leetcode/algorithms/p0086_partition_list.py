class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = ListNode(-1)
        l2 = ListNode(-1)
        less, greater = l1, l2
        current = head

        while current:
            if current.val < x:
                less.next, less = current, current
            else:
                greater.next, greater = current, current

            current = current.next

        greater.next = None
        less.next = l2.next

        return l1.next
