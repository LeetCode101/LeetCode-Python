class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) \
            -> ListNode:
        length_a = self._get_list_length(headA)
        length_b = self._get_list_length(headB)
        current1, current2 = headA, headB

        if length_a > length_b:
            for _ in range(length_a - length_b):
                current1 = current1.next
        else:
            for _ in range(length_b - length_a):
                current2 = current2.next

        while current1 and current2 and current1 != current2:
            current1 = current1.next
            current2 = current2.next

        return current1

    def _get_list_length(self, head: ListNode) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length
