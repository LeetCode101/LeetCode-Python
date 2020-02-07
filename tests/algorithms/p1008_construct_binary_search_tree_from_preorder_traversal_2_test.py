import unittest
from leetcode.algorithms\
    .p1008_construct_binary_search_tree_from_preorder_traversal_2 \
    import Solution


class TestConstructBinarySearchTreeFromPreorderTraversal(unittest.TestCase):
    def test_construct_binary_search_tree_from_preorder_traversal(self):
        solution = Solution()

        self.assertIsNone(solution.bstFromPreorder([]))
        self.assertEqual(4, solution.bstFromPreorder([4, 2]).val)
        self.assertEqual(8, solution.bstFromPreorder([8, 5, 1, 7, 10, 12]).val)
