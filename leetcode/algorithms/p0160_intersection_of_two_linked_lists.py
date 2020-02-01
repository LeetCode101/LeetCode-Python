class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) \
            -> ListNode:
        nodes = set()
        current1, current2 = headA, headB

        while current1:
            nodes.add(current1)

            current1 = current1.next

        while current2:
            if current2 in nodes:
                return current2

            current2 = current2.next

        return None
