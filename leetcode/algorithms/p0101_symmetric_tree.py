class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left_nodes = []
        right_nodes = []

        self._root_left_right(root.left, left_nodes)
        self._root_right_left(root.right, right_nodes)

        if len(left_nodes) != len(right_nodes):
            return False

        for i in range(len(left_nodes)):
            if left_nodes[i] != right_nodes[i]:
                return False

        return True

    def _root_left_right(self, root, nodes):
        if not root:
            nodes.append(None)

            return

        nodes.append(root.val)

        self._root_left_right(root.left, nodes)
        self._root_left_right(root.right, nodes)

    def _root_right_left(self, root, nodes):
        if not root:
            nodes.append(None)

            return

        nodes.append(root.val)

        self._root_right_left(root.right, nodes)
        self._root_right_left(root.left, nodes)
