# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        reversed = None
        current = head

        while slow:
            slow.next, reversed, slow = reversed, slow, slow.next

        while reversed:
            if reversed.val != current.val:
                return False

            current = current.next
            reversed = reversed.next

        return True
