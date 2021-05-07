import unittest
from leetcode.algorithms \
    .p0889_construct_binary_tree_from_preorder_and_postorder_traversal_2 \
    import Solution


class TestConstructBinaryTreeFromPreorderAndPostorderTraversal(
        unittest.TestCase):
    def test_construct_binary_tree_from_preorder_and_postorder_traversal(self):
        solution = Solution()

        self.assertEqual(1, solution.constructFromPrePost(
            [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]).val)
