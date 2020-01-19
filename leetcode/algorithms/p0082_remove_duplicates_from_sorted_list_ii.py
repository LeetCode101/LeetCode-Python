class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        prev, current = dummy, head

        while current:
            current_value = current.val

            if current.next and current_value == current.next.val:
                while current and current.val == current_value:
                    current = current.next
            else:
                prev.next, prev = current, current
                current = current.next

        prev.next = current

        return dummy.next
