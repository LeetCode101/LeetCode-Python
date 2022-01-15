from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev_value = None
        self.max_length = 0
        self.current_length = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self._inorder(root)

        return self.result

    def _inorder(self, root):
        if not root:
            return

        self._inorder(root.left)

        if self.prev_value is not None and self.prev_value == root.val:
            self.current_length += 1
        else:
            self.current_length = 1

        if self.max_length == self.current_length:
            self.result.append(root.val)
        elif self.max_length < self.current_length:
            self.max_length = self.current_length
            self.result = [root.val]

        self.prev_value = root.val

        self._inorder(root.right)
