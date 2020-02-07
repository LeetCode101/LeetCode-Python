from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        encoded = []
        queue = deque([root]) if root else deque()

        while queue:
            node = queue.popleft()

            if not node:
                encoded.append('')

                continue

            encoded.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ','.join(encoded)

    def deserialize(self, data):
        if not data:
            return None

        values = deque(data.split(','))
        root = TreeNode(int(values.popleft()))
        queue = deque([root])

        while queue and values:
            node = queue.popleft()
            left_value = values.popleft()
            right_value = values.popleft()

            if left_value != '':
                node.left = TreeNode(int(left_value))

                queue.append(node.left)

            if right_value != '':
                node.right = TreeNode(int(right_value))

                queue.append(node.right)

        return root
