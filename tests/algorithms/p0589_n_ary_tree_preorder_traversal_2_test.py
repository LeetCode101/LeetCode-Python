import unittest
from leetcode.algorithms.p0589_n_ary_tree_preorder_traversal_2 \
    import Solution, Node


class TestNAryTreePreorderTraversal(unittest.TestCase):
    def test_n_ary_tree_preorder_traversal(self):
        solution = Solution()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )

        self.assertListEqual([], solution.preorder(None))
        self.assertListEqual([1, 3, 5, 6, 2, 4], solution.preorder(root))
