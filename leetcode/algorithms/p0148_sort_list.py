from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        middle = self._find_middle(head)

        head2 = middle.next
        middle.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(head2)

        return self._merge(list1, list2)

    def _find_middle(self, head):
        slow, fast = head, head

        while slow and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, a, b):
        dummy = ListNode(0)
        current = dummy

        while a and b:
            if a.val <= b.val:
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next

            current = current.next

        current.next = a or b

        return dummy.next
