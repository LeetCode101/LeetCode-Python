import unittest
from leetcode.algorithms.p0958_check_completeness_of_a_binary_tree \
    import Solution, TreeNode


class TestCheckCompletenessOfABinaryTree(unittest.TestCase):
    def test_check_completeness_of_a_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6))
        )
        root2 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, None, TreeNode(7))
        )
        root3 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8))),
            TreeNode(3, TreeNode(7))
        )

        self.assertTrue(solution.isCompleteTree(None))
        self.assertTrue(solution.isCompleteTree(root1))
        self.assertFalse(solution.isCompleteTree(root2))
        self.assertFalse(solution.isCompleteTree(root3))
