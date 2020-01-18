class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy
        current1, current2 = l1, l2

        while current1 or current2:
            new, changed_current = None, None

            if current1 and current2:
                if current1.val <= current2.val:
                    new, current1 = current1, current1.next
                else:
                    new, current2 = current2, current2.next
            elif current1:
                new, current1 = current1, current1.next
            elif current2:
                new, current2 = current2, current2.next

            prev.next, prev = new, new

        return dummy.next
