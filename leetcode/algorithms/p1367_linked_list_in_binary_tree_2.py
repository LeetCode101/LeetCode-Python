from typing import Optional


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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) \
            -> bool:
        if not root:
            return not head

        if self._dfs(head, root):
            return True

        return self.isSubPath(head, root.left) \
            or self.isSubPath(head, root.right)

    def _dfs(self, head, root):
        if not head:
            return True

        if not root:
            return False

        if head.val != root.val:
            return False

        return self._dfs(head.next, root.left) \
            or self._dfs(head.next, root.right)
