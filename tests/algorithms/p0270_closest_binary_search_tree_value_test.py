import sys
import unittest
from leetcode.algorithms.p0270_closest_binary_search_tree_value \
    import Solution, TreeNode


class TestClosestBinarySearchTreeValue(unittest.TestCase):
    def test_closest_binary_search_tree_value(self):
        solution = Solution()
        a = TreeNode(4)
        b = TreeNode(2, TreeNode(1), TreeNode(3))
        c = TreeNode(5)
        a.left = b
        a.right = c

        self.assertEqual(sys.maxsize, solution.closestValue(None, 1))
        self.assertEqual(4, solution.closestValue(a, 3.714286))
        self.assertEqual(1, solution.closestValue(TreeNode(1), 4.428571))
