from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        numbers = self._convert_to_list(head)
        stack, result = [], [0] * len(numbers)

        for i, n in enumerate(numbers):
            while stack and numbers[stack[-1]] < n:
                result[stack.pop()] = n

            stack.append(i)

        return result

    def _convert_to_list(self, head):
        current = head
        result = []

        while current:
            result.append(current.val)
            current = current.next

        return result
