import unittest
from leetcode.algorithms.p0098_validate_binary_search_tree \
    import Solution, TreeNode


class TestValidateBinarySearchTree(unittest.TestCase):
    def test_validate_binary_search_tree(self):
        solution = Solution()
        a = TreeNode(2)
        a.left = TreeNode(1)
        a.right = TreeNode(3)

        self.assertTrue(solution.isValidBST(a))
