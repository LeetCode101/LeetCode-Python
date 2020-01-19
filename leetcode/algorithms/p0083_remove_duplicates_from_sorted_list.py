class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev, current = dummy, head

        while current:
            if prev is not dummy and prev.val == current.val:
                prev.next = None
            else:
                prev.next, prev = current, current

            current = current.next

        return dummy.next
