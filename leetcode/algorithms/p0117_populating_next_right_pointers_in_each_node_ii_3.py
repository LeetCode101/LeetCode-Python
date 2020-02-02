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

        head = root
        dummy = Node(-1)
        current = dummy

        while root:
            if root.left:
                current.next = root.left
                current = current.next

            if root.right:
                current.next = root.right
                current = current.next

            root = root.next

            if not root:
                root = dummy.next
                dummy.next = None
                current = dummy

        return head
