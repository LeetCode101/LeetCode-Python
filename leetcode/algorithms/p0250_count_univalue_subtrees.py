class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self._is_uni(root)

        return self.count

    def _is_uni(self, root):
        if not root:
            return True

        is_left_uni = not root.left \
            or (self._is_uni(root.left) and root.val == root.left.val)
        is_right_uni = not root.right \
            or (self._is_uni(root.right) and root.val == root.right.val)

        if is_left_uni and is_right_uni:
            self.count += 1

            return True
        else:
            return False
