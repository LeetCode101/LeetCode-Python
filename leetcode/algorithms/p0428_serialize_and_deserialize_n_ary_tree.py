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
        return self._deserialize(deque(data.split(',')))

    def _preorder(self, root, encoded):
        encoded.append(str(root.val))

        if root.children:
            encoded.append(str(len(root.children)))

            for child in root.children:
                self._preorder(child, encoded)
        else:
            encoded.append('0')

    def _deserialize(self, encoded):
        root_value = int(encoded.popleft())
        children_size = int(encoded.popleft())
        root = Node(root_value)

        if children_size == 0:
            return root

        root.children = [self._deserialize(encoded)
                         for _ in range(children_size)]

        return root
