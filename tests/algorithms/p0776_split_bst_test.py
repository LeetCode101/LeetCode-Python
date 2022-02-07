import unittest
from leetcode.algorithms.p0776_split_bst import Solution, TreeNode


class TestSplitBST(unittest.TestCase):
    def test_split_bst(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7))
        )

        self.assertListEqual([2, 4], list(map(lambda x: x.val,
                                              solution.splitBST(root, 2))))
