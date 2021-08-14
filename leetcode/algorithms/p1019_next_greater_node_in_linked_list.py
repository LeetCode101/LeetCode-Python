from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        stack = []
        result = [0] * self._get_length(head)
        numbers = []
        current = head
        i = 0

        while current:
            while stack and numbers[stack[-1]] < current.val:
                result[stack.pop()] = current.val

            stack.append(i)
            numbers.append(current.val)
            current = current.next
            i += 1

        return result

    def _get_length(self, head):
        current = head
        length = 0

        while current:
            length += 1
            current = current.next

        return length
