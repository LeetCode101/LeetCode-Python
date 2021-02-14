# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        is_odd = False
        odd_tail = head
        even_tail = head.next
        current = head.next

        while current:
            if is_odd:
                odd_tail.next, current.next, current = \
                    current, odd_tail.next, current.next
                odd_tail = odd_tail.next
                even_tail.next, even_tail = current, current
            else:
                current = current.next

            is_odd = not is_odd

        return head
