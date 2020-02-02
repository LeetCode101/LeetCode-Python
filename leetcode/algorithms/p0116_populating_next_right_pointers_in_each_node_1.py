from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        queue = deque([root]) if root else deque()

        while queue:
            prev = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if not prev:
                    prev = node
                else:
                    prev.next, prev = node, node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
