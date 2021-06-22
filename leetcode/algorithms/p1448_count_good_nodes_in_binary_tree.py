class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self._dfs(root, root.val)

    def _dfs(self, root, max_so_far):
        count = 1 if root.val >= max_so_far else 0

        if root.left:
            count += self._dfs(root.left, max(root.val, max_so_far))

        if root.right:
            count += self._dfs(root.right, max(root.val, max_so_far))

        return count
