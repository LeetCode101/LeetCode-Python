import unittest
from leetcode.algorithms.p0096_unique_binary_search_trees import Solution


class TestUniqueBinarySearchTrees(unittest.TestCase):
    def test_unique_binary_search_trees(self):
        solution = Solution()

        self.assertEqual(5, solution.numTrees(3))
        self.assertEqual(1, solution.numTrees(1))
