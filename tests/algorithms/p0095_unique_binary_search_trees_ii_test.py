import unittest
from leetcode.algorithms.p0095_unique_binary_search_trees_ii \
    import Solution
from tests.algorithms.binary_tree_helper import inorder


class TestUniqueBinarySearchTrees(unittest.TestCase):
    def test_unique_binary_search_trees(self):
        solution = Solution()

        self.assertListEqual([1, 2, 3], inorder(solution.generateTrees(3)[0]))
