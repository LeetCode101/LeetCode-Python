import unittest
from leetcode.algorithms.p1104_path_in_zigzag_labelled_binary_tree_2 \
    import Solution


class TestPathInZigzagLabelledBinaryTree(unittest.TestCase):
    def test_path_in_zigzag_labelled_binary_tree(self):
        solution = Solution()

        self.assertListEqual([1, 3, 4, 14], solution.pathInZigZagTree(14))
        self.assertListEqual([1, 2, 6, 10, 26], solution.pathInZigZagTree(26))
