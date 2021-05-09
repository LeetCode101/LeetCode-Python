import unittest
from leetcode.algorithms.p0700_search_in_a_binary_search_tree \
    import Solution, TreeNode


class TestSearchInABinarySearchTree(unittest.TestCase):
    def test_search_in_a_binary_search_tree(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7)
        )

        self.assertEqual(2, solution.searchBST(root, 2).val)
        self.assertIsNone(solution.searchBST(root, 5))
