from collections import deque
from typing import Deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        encoded = deque()

        self._preorder(root, encoded)

        return ','.join(list(encoded))

    def deserialize(self, data):
        return self._deserialize(deque(data.split(',')))

    def _preorder(self, root: TreeNode, encoded: Deque) -> None:
        if not root:
            encoded.append('')
        else:
            encoded.append(str(root.val))

            self._preorder(root.left, encoded)
            self._preorder(root.right, encoded)

    def _deserialize(self, encoded: Deque) -> TreeNode:
        if encoded[0] == '':
            encoded.popleft()

            return None

        root_value = int(encoded.popleft())
        root = TreeNode(root_value)
        root.left = self._deserialize(encoded)
        root.right = self._deserialize(encoded)

        return root
