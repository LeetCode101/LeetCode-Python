import unittest
from leetcode.algorithms.p1457_pseudo_palindromic_paths_in_a_binary_tree_3 \
    import Solution, TreeNode


class TestPseudoPalindromicPathsInABinaryTree(unittest.TestCase):
    def test_pseudo_palindromic_paths_in_a_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            2,
            TreeNode(3, TreeNode(3), TreeNode(1)),
            TreeNode(1, None, TreeNode(1))
        )
        root2 = TreeNode(
            2,
            TreeNode(
                1,
                TreeNode(1),
                TreeNode(3, None, TreeNode(1))
            ),
            TreeNode(1)
        )

        self.assertEqual(0, solution.pseudoPalindromicPaths(None))
        self.assertEqual(1, solution.pseudoPalindromicPaths(root2))
        self.assertEqual(2, solution.pseudoPalindromicPaths(root1))
