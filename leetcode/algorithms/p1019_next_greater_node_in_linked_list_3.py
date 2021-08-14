from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, result = [], []
        i = 0
        current = head

        while current:
            result.append(0)

            while stack and stack[-1][1] < current.val:
                result[stack.pop()[0]] = current.val

            stack.append((i, current.val))
            current = current.next
            i += 1

        return result
