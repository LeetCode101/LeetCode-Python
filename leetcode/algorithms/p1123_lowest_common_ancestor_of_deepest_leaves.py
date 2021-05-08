class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self._dfs(root)[1]

    def _dfs(self, root):
        if not root:
            return 0, None

        h1, lca1 = self._dfs(root.left)
        h2, lca2 = self._dfs(root.right)

        if h1 > h2:
            return h1 + 1, lca1

        if h1 < h2:
            return h2 + 1, lca2

        return h1 + 1, root
