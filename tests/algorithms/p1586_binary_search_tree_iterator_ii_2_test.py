import unittest
from leetcode.algorithms.p1586_binary_search_tree_iterator_ii_2 \
    import BSTIterator, TreeNode


class TestBinarySearchTreeIterator(unittest.TestCase):
    def testbinary_search_tree_iterator(self):
        root = TreeNode(
            7,
            TreeNode(3),
            TreeNode(15, TreeNode(9), TreeNode(20))
        )
        bst_iterator = BSTIterator(root)

        self.assertEqual(3, bst_iterator.next())
        self.assertEqual(7, bst_iterator.next())
        self.assertTrue(bst_iterator.hasNext())
        self.assertTrue(bst_iterator.hasPrev())
        self.assertEqual(3, bst_iterator.prev())
