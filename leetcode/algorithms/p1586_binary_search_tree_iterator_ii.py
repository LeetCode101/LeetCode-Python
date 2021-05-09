class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes = []
        self._inorder(root, self.nodes)
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.nodes)

    def next(self) -> int:
        self.pointer += 1

        return self.nodes[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer - 1 >= 0

    def prev(self) -> int:
        self.pointer -= 1

        return self.nodes[self.pointer]

    def _inorder(self, root, nodes):
        if not root:
            return

        self._inorder(root.left, nodes)
        nodes.append(root.val)
        self._inorder(root.right, nodes)
