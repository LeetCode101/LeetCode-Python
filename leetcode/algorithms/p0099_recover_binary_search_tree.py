from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        self._inorder(root, nodes)

        for i in range(len(nodes) - 1):
            if nodes[i].val <= nodes[i + 1].val:
                continue

            j = i + 1

            while j < len(nodes) and nodes[i].val > nodes[j].val:
                j += 1

            nodes[i].val, nodes[j - 1].val = nodes[j - 1].val, nodes[i].val

            break

    def _inorder(self, root, nodes):
        if not root:
            return

        self._inorder(root.left, nodes)

        nodes.append(root)

        self._inorder(root.right, nodes)
