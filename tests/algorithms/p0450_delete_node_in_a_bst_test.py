import unittest
from leetcode.algorithms.p0450_delete_node_in_a_bst import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestDeleteNodeInABST(unittest.TestCase):
    def test_delete_node_in_a_bst(self):
        solution = Solution()
        root = TreeNode(
            5,
            TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3))),
            TreeNode(6, None, TreeNode(7))
        )

        self.assertListEqual([1, 3, 4, 5, 6, 7],
                             inorder(solution.deleteNode(root, 2)))
