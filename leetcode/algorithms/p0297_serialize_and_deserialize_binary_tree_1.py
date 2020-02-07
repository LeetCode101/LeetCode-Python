from typing import List, Deque
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        encoded = deque()

        self.preorder(root, encoded)

        return ','.join(list(encoded))

    def deserialize(self, data):
        return self.deserialize_internal(deque(data.split(',')))

    def preorder(self, root: TreeNode, encoded: Deque) -> None:
        if not root:
            encoded.append('')
        else:
            encoded.append(str(root.val))

            self.preorder(root.left, encoded)
            self.preorder(root.right, encoded)

    def deserialize_internal(self, encoded: Deque) -> TreeNode:
        if encoded[0] == '':
            encoded.popleft()

            return None

        root_value = int(encoded.popleft())
        root = TreeNode(root_value)
        root.left = self.deserialize_internal(encoded)
        root.right = self.deserialize_internal(encoded)

        return root
