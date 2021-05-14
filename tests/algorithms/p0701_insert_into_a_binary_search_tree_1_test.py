import unittest
from leetcode.algorithms.p0701_insert_into_a_binary_search_tree_1 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestInsertIntoABinarySearchTree(unittest.TestCase):
    def test_insert_into_a_binary_search_tree(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7)
        )

        self.assertListEqual([1, 2, 3, 4, 5, 7],
                             inorder(solution.insertIntoBST(root, 5)))
