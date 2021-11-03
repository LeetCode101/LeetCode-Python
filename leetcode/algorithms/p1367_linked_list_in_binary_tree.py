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


# Time Limit Exceeded!
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) \
            -> bool:
        if not head:
            return True

        if not root:
            return False

        if root.val == head.val:
            return self.isSubPath(head.next, root.left) \
                   or self.isSubPath(head.next, root.right) \
                   or self.isSubPath(head, root.left) \
                   or self.isSubPath(head, root.right)
        else:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
