import unittest
from leetcode.algorithms.p0669_trim_a_binary_search_tree \
    import Solution, TreeNode


class TestTrimABinarySearchTree(unittest.TestCase):
    def test_trim_a_binary_search_tree(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(0)
        c = TreeNode(4)
        a.left = b
        a.right = c
        d = TreeNode(2)
        b.right = d
        d.left = TreeNode(1)

        self.assertEqual(3, solution.trimBST(a, 1, 3).val)
