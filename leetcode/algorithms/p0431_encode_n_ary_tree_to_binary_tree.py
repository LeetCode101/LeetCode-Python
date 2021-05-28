class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        binary_tree = TreeNode(root.val)

        if not root.children:
            return binary_tree

        binary_tree.left = self.encode(root.children[0])
        node = binary_tree.left

        for child in root.children[1:]:
            node.right = self.encode(child)
            node = node.right

        return binary_tree

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None

        n_ary_tree = Node(data.val, [])
        node = data.left

        while node:
            n_ary_tree.children.append(self.decode(node))
            node = node.right

        return n_ary_tree
