import unittest
from leetcode.algorithms.p0590_n_ary_tree_postorder_traversal_2 \
    import Solution, Node


class TestNAryTreePostorderTraversal(unittest.TestCase):
    def test_n_ary_tree_postorder_traversal(self):
        solution = Solution()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )

        self.assertListEqual([], solution.postorder(None))
        self.assertListEqual([5, 6, 3, 2, 4, 1], solution.postorder(root))
