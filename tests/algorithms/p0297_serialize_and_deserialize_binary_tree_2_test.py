import unittest
from leetcode.algorithms.p0297_serialize_and_deserialize_binary_tree_2 \
    import Codec, TreeNode


class TestSerializeAndDeserializeBinaryTree(unittest.TestCase):
    def test_serialize_and_deserialize_binary_tree(self):
        a = TreeNode(1)
        a.left = TreeNode(2)
        a.right = TreeNode(3)
        codec = Codec()
        encoded = codec.serialize(a)

        self.assertIsNone(codec.deserialize(''))
        self.assertEqual(1, codec.deserialize(encoded).val)
