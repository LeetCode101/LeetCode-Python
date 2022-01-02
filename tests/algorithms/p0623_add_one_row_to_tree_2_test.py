import unittest
from leetcode.algorithms.p0623_add_one_row_to_tree_2 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestAddOneRowToTree(unittest.TestCase):
    def test_add_one_row_to_tree(self):
        solution = Solution()
        root1 = TreeNode(
            4,
            TreeNode(2, TreeNode(3), TreeNode(1)),
            TreeNode(6, TreeNode(5))
        )
        root2 = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3)
        )
        root3 = TreeNode(
            1,
            None,
            TreeNode(2)
        )

        self.assertListEqual([1, 2, 2],
                             inorder(solution.addOneRow(root3, 2, 1)))
        self.assertListEqual([5, 4, 5, 2, 1, 3],
                             inorder(solution.addOneRow(root2, 5, 4)))
        self.assertListEqual([3, 2, 1, 1, 4, 1, 5, 6],
                             inorder(solution.addOneRow(root1, 1, 2)))
