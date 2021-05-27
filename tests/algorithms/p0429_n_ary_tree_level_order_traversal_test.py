import unittest
from leetcode.algorithms.p0429_n_ary_tree_level_order_traversal \
    import Solution, Node


class TestNAryTreeLevelOrderTraversal(unittest.TestCase):
    def test_n_ary_tree_level_order_traversal(self):
        solution = Solution()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )

        self.assertListEqual([], solution.levelOrder(None))
        self.assertListEqual([[1], [3, 2, 4], [5, 6]],
                             solution.levelOrder(root))
