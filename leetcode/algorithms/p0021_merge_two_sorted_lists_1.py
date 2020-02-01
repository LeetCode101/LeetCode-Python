class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy
        current1, current2 = l1, l2

        while current1 and current2:
            new = None

            if current1.val <= current2.val:
                new, current1 = current1, current1.next
            else:
                new, current2 = current2, current2.next

            prev.next, prev = new, new

        prev.next = current1 or current2

        return dummy.next
