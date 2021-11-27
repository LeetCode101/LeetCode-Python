import unittest
from leetcode.algorithms.p1026_maximum_difference_between_node_and_ancestor_2 \
    import Solution, TreeNode


class TestMaximumDifferenceBetweenNodeAndAncestor(unittest.TestCase):
    def test_maximum_difference_between_node_and_ancestor(self):
        solution = Solution()
        root = TreeNode(
            8,
            TreeNode(
                3,
                TreeNode(1),
                TreeNode(6, TreeNode(4), TreeNode(7))
            ),
            TreeNode(10, None, TreeNode(14, TreeNode(13)))
        )

        self.assertEqual(7, solution.maxAncestorDiff(root))
