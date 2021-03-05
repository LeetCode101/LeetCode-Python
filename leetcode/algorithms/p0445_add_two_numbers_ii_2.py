from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = self._convert_list_to_stack(l1), \
                         self._convert_list_to_stack(l2)
        prev = None
        carry = 0

        while stack1 or stack2:
            sum = carry

            if stack1:
                sum += stack1.pop()

            if stack2:
                sum += stack2.pop()

            carry = sum // 10
            new = ListNode(sum % 10)
            new.next, prev = prev, new

        if carry != 0:
            new = ListNode(carry)
            new.next, prev = prev, new

        return prev

    def _convert_list_to_stack(self, head: ListNode) -> List[int]:
        stack, current = [], head

        while current:
            stack.append(current.val)

            current = current.next

        return stack
