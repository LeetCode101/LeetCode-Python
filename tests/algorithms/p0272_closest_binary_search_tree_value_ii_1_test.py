import unittest
from leetcode.algorithms.p0272_closest_binary_search_tree_value_ii_1 \
    import Solution, TreeNode


class TestClosestBinarySearchTreeValue(unittest.TestCase):
    def test_closest_binary_search_tree_value(self):
        solution = Solution()
        a = TreeNode(4)
        b = TreeNode(2, TreeNode(1), TreeNode(3))
        c = TreeNode(5)
        a.left = b
        a.right = c

        self.assertListEqual([3, 4], sorted(solution.closestKValues(
            a, 3.714286, 2)))
        self.assertListEqual([1], solution.closestKValues(
            TreeNode(1), 0.000000, 1))
