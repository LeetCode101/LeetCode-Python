class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tail = head.next
        prev_tail = head

        while tail:
            rest = tail.next
            prev = dummy

            while prev.next is not tail and prev.next.val <= tail.val:
                prev = prev.next

            if prev.next is tail:
                prev_tail = tail
                tail = rest

                continue

            prev.next, tail.next = tail, prev.next

            if prev_tail:
                prev_tail.next = rest
                tail = rest

        return dummy.next
