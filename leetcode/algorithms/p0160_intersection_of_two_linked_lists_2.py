class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) \
            -> ListNode:
        current1, current2 = headA, headB

        while current1 != current2:
            current1 = current1.next if current1 else headB
            current2 = current2.next if current2 else headA

        return current1
