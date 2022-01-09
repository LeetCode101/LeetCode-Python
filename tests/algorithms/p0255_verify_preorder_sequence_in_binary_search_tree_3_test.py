import unittest
from leetcode.algorithms\
    .p0255_verify_preorder_sequence_in_binary_search_tree_3 import Solution


class TestVerifyPreorderSequenceInBinarySearchTree(unittest.TestCase):
    def test_verify_preorder_sequence_in_binary_search_tree(self):
        solution = Solution()

        self.assertTrue(solution.verifyPreorder([5, 2, 1, 3, 6]))
        self.assertFalse(solution.verifyPreorder([5, 2, 6, 1, 3]))
