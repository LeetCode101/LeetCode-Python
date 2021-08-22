class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tail = head.next

        while tail:
            rest = tail.next
            prev = dummy

            while prev.next is not tail and prev.next.val <= tail.val:
                prev = prev.next

            current_tail = prev.next

            while current_tail and current_tail.next is not tail:
                current_tail = current_tail.next

            if prev.next is tail:
                tail = rest

                continue

            prev.next, tail.next = tail, prev.next

            if current_tail:
                current_tail.next = rest
                tail = rest

        return dummy.next
