import unittest
from leetcode.algorithms \
    .p0106_construct_binary_tree_from_inorder_and_postorder_traversal \
    import Solution


class TestConstructBinaryTreeFromInorderAndPostorderTraversal(
        unittest.TestCase):
    def test_construct_binary_tree_from_inorder_and_postorder_traversal(self):
        solution = Solution()

        self.assertEqual(3, solution.buildTree(
            [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]).val)
