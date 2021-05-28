import unittest
from leetcode.algorithms.p0428_serialize_and_deserialize_n_ary_tree_1 \
    import Codec, Node


class TestSerializeAndDeserializeNAryTree(unittest.TestCase):
    def test_serialize_and_deserialize_n_ary_tree(self):
        codec = Codec()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )
        encoded = codec.serialize(root)

        self.assertEqual('', codec.serialize(None))
        self.assertIsNone(codec.deserialize(''))
        self.assertEqual('1,3,5,,6,,,2,,4,,', encoded)
        self.assertEqual(1, codec.deserialize(encoded).val)
