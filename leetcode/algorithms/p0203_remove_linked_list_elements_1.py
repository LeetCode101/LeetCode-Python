# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, next=head)
        prev, current = dummy, head

        while current:
            if current.val != val:
                prev = current
            else:
                prev.next = current.next

            current = current.next

        return dummy.next
