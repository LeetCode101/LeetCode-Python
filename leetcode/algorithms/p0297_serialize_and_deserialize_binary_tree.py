from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        encoded = []

        self.serialize_internal(root, encoded)

        return ','.join(encoded)

    def deserialize(self, data):
        return self.deserialize_internal(data.split(','))

    def serialize_internal(self, root: TreeNode, encoded: List[str]) -> None:
        if not root:
            encoded.append('')
        else:
            encoded.append(str(root.val))

            self.serialize_internal(root.left, encoded)
            self.serialize_internal(root.right, encoded)

    def deserialize_internal(self, encoded: List[str]) -> TreeNode:
        if encoded[0] == '':
            encoded.pop(0)

            return None

        root_value = int(encoded.pop(0))
        root = TreeNode(root_value)
        root.left = self.deserialize_internal(encoded)
        root.right = self.deserialize_internal(encoded)

        return root
