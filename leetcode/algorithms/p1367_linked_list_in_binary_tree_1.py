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
        return self._dfs(head, root, True)

    def _dfs(self, head, root, is_head):
        if not head:
            return True

        if not root:
            return False

        if root.val == head.val:
            if is_head:
                return self._dfs(head.next, root.left, False) \
                       or self._dfs(head.next, root.right, False) \
                       or self._dfs(head, root.left, True) \
                       or self._dfs(head, root.right, True)
            else:
                return self._dfs(head.next, root.left, False) \
                       or self._dfs(head.next, root.right, False)
        else:
            if is_head:
                return self._dfs(head, root.left, True) \
                       or self._dfs(head, root.right, True)
            else:
                return False
