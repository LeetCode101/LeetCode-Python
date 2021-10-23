from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        self._dfs(root, nodes)

        return nodes

    def _dfs(self, node, nodes):
        if not node:
            return

        if (node.left and not node.right) \
                or (node.right and not node.left):
            nodes.append(node.left.val if node.left else node.right.val)

        if node.left:
            self._dfs(node.left, nodes)

        if node.right:
            self._dfs(node.right, nodes)

        return nodes
