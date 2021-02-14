# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        is_odd = True
        current = head
        odd, head_of_even = ListNode(-1), ListNode(-1)
        even = head_of_even

        while current:
            if is_odd:
                odd.next, odd = current, current
            else:
                even.next, even = current, current

            is_odd = not is_odd
            current = current.next

        odd.next = head_of_even.next
        even.next = None

        return head
