import unittest
from leetcode.algorithms.p0449_serialize_and_deserialize_bst \
    import Codec, TreeNode


class TestSerializeAndDeserializeBST(unittest.TestCase):
    def test_serialize_and_deserialize_bst(self):
        a = TreeNode(1)
        a.left = TreeNode(2)
        a.right = TreeNode(3)
        codec = Codec()
        encoded = codec.serialize(a)

        self.assertIsNone(codec.deserialize(''))
        self.assertEqual(1, codec.deserialize(encoded).val)
