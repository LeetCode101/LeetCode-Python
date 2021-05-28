import unittest
from leetcode.algorithms.p0431_encode_n_ary_tree_to_binary_tree \
    import Codec, Node
from tests.algorithms.binary_tree_helper import inorder


class TestEncodeNAryTreeToBinaryTree(unittest.TestCase):
    def test_encode_n_ary_tree_to_binary_tree(self):
        codec = Codec()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )
        binary_tree = codec.encode(root)

        self.assertIsNone(codec.encode(None))
        self.assertIsNone(codec.decode(None))
        self.assertListEqual([5, 6, 3, 2, 4, 1], inorder(binary_tree))
        self.assertEqual(1, codec.decode(binary_tree).val)
