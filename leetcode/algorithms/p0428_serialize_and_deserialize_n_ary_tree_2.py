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
        queue = deque([root]) if root else deque()

        while queue:
            node = queue.popleft()

            if not node:
                encoded.append('')

                continue

            encoded.append(str(node.val))

            if node.children:
                for child in node.children:
                    queue.append(child)

            queue.append(None)

        return ','.join(encoded)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        encoded = deque(data.split(','))
        root = Node(int(encoded.popleft()), [])
        queue = deque([root])

        while queue and encoded:
            node = queue.popleft()

            while encoded[0] != '':
                child = Node(int(encoded.popleft()), [])
                node.children.append(child)
                queue.append(child)

            encoded.popleft()

        return root
