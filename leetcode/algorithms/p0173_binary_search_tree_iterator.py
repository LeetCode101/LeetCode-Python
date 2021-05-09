class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes = []
        self._inorder(root, self.nodes)
        self.pointer = 0

    def next(self) -> int:
        value = self.nodes[self.pointer]
        self.pointer += 1

        return value

    def hasNext(self) -> bool:
        return self.pointer < len(self.nodes)

    def _inorder(self, root, nodes):
        if not root:
            return

        self._inorder(root.left, nodes)
        nodes.append(root.val)
        self._inorder(root.right, nodes)
