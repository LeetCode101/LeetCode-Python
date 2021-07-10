class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self._dfs(root, subRoot, False)

    def _dfs(self, root, sub_root, need_continuous):
        if not root:
            return not sub_root

        if not sub_root:
            return False

        if root.val == sub_root.val \
                and self._dfs(root.left, sub_root.left, True) \
                and self._dfs(root.right, sub_root.right, True):
            return True

        if need_continuous:
            return False
        else:
            return self._dfs(root.left, sub_root, False) \
                   or self._dfs(root.right, sub_root, False)
