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

        left_most = root

        while left_most.left:
            current = left_most

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next

            left_most = left_most.left

        return root
