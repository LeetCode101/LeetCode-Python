import unittest
from leetcode.algorithms\
    .p0105_construct_binary_tree_from_preorder_and_inorder_traversal \
    import Solution


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(
      unittest.TestCase):
    def test_construct_binary_tree_from_preorder_and_inorder_traversal(self):
        solution = Solution()

        self.assertEqual(
            3, solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)
