# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        current = head

        while current:
            stack.append(current.val)

            current = current.next

        current = head

        for i in range(len(stack) - 1, len(stack) // 2 - 1, -1):
            if stack[i] != current.val:
                return False

            current = current.next

        return True
