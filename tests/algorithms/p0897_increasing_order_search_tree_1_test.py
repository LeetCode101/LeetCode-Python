import unittest
from leetcode.algorithms.p0897_increasing_order_search_tree_1 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestIncreasingOrderSearchTree(unittest.TestCase):
    def test_increasing_order_search_tree(self):
        solution = Solution()
        root = TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(2, TreeNode(1)),
                TreeNode(4)
            ),
            TreeNode(
                6,
                None,
                TreeNode(8, TreeNode(7), TreeNode(9))
            )
        )

        self.assertListEqual(list(range(1, 10)),
                             inorder(solution.increasingBST(root)))
        self.assertListEqual([], inorder(solution.increasingBST(None)))
