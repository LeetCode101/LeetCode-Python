class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        current = head
        i, mapping = 0, {}

        while current:
            i += 1
            mapping[i] = current
            current = current.next

        step = k % i

        if step == 0:
            return head

        index_to_cut = i - step
        mapping[i].next = head
        mapping[index_to_cut].next = None

        return mapping[min(i, index_to_cut + 1)]
