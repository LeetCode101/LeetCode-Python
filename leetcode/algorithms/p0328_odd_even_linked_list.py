# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 1
        current = head
        odd, head_of_even = ListNode(-1), ListNode(-1)
        even = head_of_even

        while current:
            if i & 1 == 1:
                odd.next, odd = current, current
            else:
                even.next, even = current, current

            i += 1
            current = current.next

        odd.next = head_of_even.next
        even.next = None

        return head
