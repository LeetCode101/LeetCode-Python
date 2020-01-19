class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = head
        i, mapping = 1, {0: dummy}

        while current:
            mapping[i] = current
            current = current.next
            i += 1

        index_to_delete = len(mapping) - n
        mapping[index_to_delete - 1].next = \
            mapping.get(index_to_delete + 1, None)

        return dummy.next
