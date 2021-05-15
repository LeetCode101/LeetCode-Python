class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        return self._sorted_list_to_bst(head, None)

    def _sorted_list_to_bst(self, head, tail):
        if head is tail:
            return None

        slow, fast = head, head

        while fast is not tail and fast.next is not tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self._sorted_list_to_bst(head, slow)
        root.right = self._sorted_list_to_bst(slow.next, tail)

        return root
