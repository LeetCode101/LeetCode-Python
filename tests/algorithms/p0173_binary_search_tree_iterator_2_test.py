import unittest
from leetcode.algorithms.p0173_binary_search_tree_iterator_2 \
    import BSTIterator, TreeNode


class TestBinarySearchTreeIterator(unittest.TestCase):
    def test_binary_search_tree_iterator(self):
        root = TreeNode(
            7,
            TreeNode(3),
            TreeNode(15, TreeNode(9), TreeNode(20))
        )
        bst_iterator = BSTIterator(root)

        self.assertEqual(3, bst_iterator.next())
        self.assertEqual(7, bst_iterator.next())
        self.assertTrue(bst_iterator.hasNext())
