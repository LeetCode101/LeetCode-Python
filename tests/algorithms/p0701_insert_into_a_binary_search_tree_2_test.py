import unittest
from leetcode.algorithms.p0701_insert_into_a_binary_search_tree_2 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestInsertIntoABinarySearchTree(unittest.TestCase):
    def test_insert_into_a_binary_search_tree(self):
        solution = Solution()
        root1 = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7)
        )
        root2 = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7)
        )

        self.assertEqual([1], inorder(solution.insertIntoBST(None, 1)))
        self.assertListEqual([1, 2, 3, 4, 5, 7],
                             inorder(solution.insertIntoBST(root1, 5)))
        self.assertListEqual([1, 2, 3, 4, 7, 8],
                             inorder(solution.insertIntoBST(root2, 8)))
