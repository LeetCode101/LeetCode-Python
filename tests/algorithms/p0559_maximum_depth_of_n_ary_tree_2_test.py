import unittest
from leetcode.algorithms.p0559_maximum_depth_of_n_ary_tree_2 \
    import Solution, Node


class TestMaximumDepthOfNAryTree(unittest.TestCase):
    def test_maximum_depth_of_n_ary_tree(self):
        solution = Solution()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )

        self.assertEqual(0, solution.maxDepth(None))
        self.assertEqual(3, solution.maxDepth(root))
