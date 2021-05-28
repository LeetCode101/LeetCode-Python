from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        encoded = deque()

        self._preorder(root, encoded)

        return ','.join(list(encoded))

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        return self._deserialize(deque(data.split(',')))

    def _preorder(self, root, encoded):
        if not root:
            return ''

        encoded.append(str(root.val))

        if root.children:
            for child in root.children:
                self._preorder(child, encoded)

        encoded.append('')

    def _deserialize(self, encoded):
        root_value = int(encoded.popleft())
        root = Node(root_value, [])

        while encoded[0] != '':
            child = self._deserialize(encoded)
            root.children.append(child)

        encoded.popleft()

        return root
