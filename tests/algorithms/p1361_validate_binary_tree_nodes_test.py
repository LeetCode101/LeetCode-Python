import unittest
from leetcode.algorithms.p1361_validate_binary_tree_nodes import Solution


class TestValidateBinaryTreeNodes(unittest.TestCase):
    def test_validate_binary_tree_nodes(self):
        solution = Solution()

        self.assertTrue(solution.validateBinaryTreeNodes(
            4, [1, -1, 3, -1], [2, -1, -1, -1]))
        self.assertTrue(solution.validateBinaryTreeNodes(
            4, [1, -1, 3, -1], [2, 3, -1, -1]))
        self.assertTrue(solution.validateBinaryTreeNodes(
            2, [1, 0], [-1, -1]))
        self.assertTrue(solution.validateBinaryTreeNodes(
            6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))
