class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self._dfs(root).node

    def _dfs(self, root):
        if not root:
            return Node(None, 0)

        left = self._dfs(root.left)
        right = self._dfs(root.right)

        if left.depth == right.depth:
            return Node(root, left.depth + 1)
        elif left.depth > right.depth:
            return Node(left.node, left.depth + 1)
        else:
            return Node(right.node, right.depth + 1)
