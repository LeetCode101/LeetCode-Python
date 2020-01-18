class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        old_head = head
        prev, current = None, head
        tail_of_left, tail_of_reverse_list = None, None

        for i in range(1, n + 1):
            if i < m:
                tail_of_left, current = current, current.next
            elif i >= m:
                if i == m:
                    tail_of_reverse_list = current

                next, current.next = current.next, prev
                prev, current = current, next

        if tail_of_left:
            tail_of_left.next = prev

        tail_of_reverse_list.next = current

        return old_head if tail_of_left else prev
