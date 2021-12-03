import unittest
from leetcode.algorithms.p1038_binary_search_tree_to_greater_sum_tree_3 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestBinarySearchTreeToGreaterSumTree(unittest.TestCase):
    def test_binary_search_tree_to_greater_sum_tree(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(
                1,
                TreeNode(0),
                TreeNode(2, None, TreeNode(3))
            ),
            TreeNode(
                6,
                TreeNode(5),
                TreeNode(7, None, TreeNode(8))
            )
        )

        self.assertListEqual([36, 36, 35, 33, 30, 26, 21, 15, 8],
                             inorder(solution.bstToGst(root)))
