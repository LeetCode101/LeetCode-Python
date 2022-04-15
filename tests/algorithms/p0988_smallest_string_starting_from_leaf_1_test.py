import unittest
from leetcode.algorithms.p0988_smallest_string_starting_from_leaf_1 \
    import Solution, TreeNode


class TestSmallestStringStartingFromLeaf(unittest.TestCase):
    def test_smallest_string_starting_from_leaf(self):
        solution = Solution()
        root = TreeNode(
            25,
            TreeNode(1, TreeNode(1), TreeNode(3)),
            TreeNode(3, TreeNode(0), TreeNode(2))
        )

        self.assertEqual('adz', solution.smallestFromLeaf(root))
