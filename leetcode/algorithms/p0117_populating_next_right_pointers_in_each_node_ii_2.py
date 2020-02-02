class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        if root.left:
            root.left.next = root.right or self.search_next(root.next)

        if root.right:
            root.right.next = self.search_next(root.next)

        self.connect(root.right)
        self.connect(root.left)

        return root

    def search_next(self, root: Node) -> Node:
        while root:
            if root.left or root.right:
                return root.left or root.right

            root = root.next

        return root
