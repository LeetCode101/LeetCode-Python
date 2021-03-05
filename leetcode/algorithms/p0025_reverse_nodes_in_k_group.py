class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        groups = self._get_list_length(head) // k
        dummy = ListNode(-1)
        dummy.next = head
        tail_of_prev_groups, tail_of_current_group = dummy, dummy.next

        for _ in range(groups):
            for i in range(k - 1):
                next = tail_of_current_group.next
                tail_of_current_group.next = next.next
                next.next, tail_of_prev_groups.next = \
                    tail_of_prev_groups.next, next

            tail_of_prev_groups, tail_of_current_group = \
                tail_of_current_group, tail_of_current_group.next

        return dummy.next

    def _get_list_length(self, head: ListNode) -> int:
        count, current = 0, head

        while current:
            count, current = count + 1, current.next

        return count
