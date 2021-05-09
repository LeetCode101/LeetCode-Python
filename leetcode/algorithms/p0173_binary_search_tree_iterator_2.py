class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes = []
        current = root

        while current:
            self.nodes.append(current)
            current = current.left

    def next(self) -> int:
        top = self.nodes.pop()
        current = top.right

        while current:
            self.nodes.append(current)
            current = current.left

        return top.val

    def hasNext(self) -> bool:
        return len(self.nodes) > 0
