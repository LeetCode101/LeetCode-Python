class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        current = head
        i, index_to_node = 0, {}

        while current:
            i += 1
            index_to_node[i] = current
            current = current.next

        step = k % i

        if step == 0:
            return head

        index_to_cut = i - step
        index_to_node[i].next = head
        index_to_node[index_to_cut].next = None

        return index_to_node[index_to_cut + 1]
