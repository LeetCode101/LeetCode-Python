from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        current = slow.next

        while current:
            stack.append(current)
            current = current.next

        current = head
        slow.next = None

        while stack:
            insert_node = stack.pop()
            next_node = current.next
            current.next, current = insert_node, current.next
            insert_node.next = next_node

        return head
