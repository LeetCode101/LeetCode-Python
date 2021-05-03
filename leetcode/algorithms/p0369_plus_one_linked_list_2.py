class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        last_not_9 = dummy
        dummy.next = head
        current = head

        while current:
            if current.val != 9:
                last_not_9 = current

            current = current.next

        last_not_9.val += 1
        current = last_not_9.next

        while current:
            current.val = 0
            current = current.next

        return dummy if dummy.val == 1 else head
