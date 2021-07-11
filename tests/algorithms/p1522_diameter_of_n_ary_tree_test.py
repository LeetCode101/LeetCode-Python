import unittest
from leetcode.algorithms.p1522_diameter_of_n_ary_tree import Solution, Node


class TestDiameterOfNAryTree(unittest.TestCase):
    def test_diameter_of_n_ary_tree(self):
        solution = Solution()
        root = Node(
            1,
            children=[
                Node(3, children=[Node(5), Node(6)]),
                Node(2),
                Node(4)
            ]
        )

        self.assertEqual(0, solution.diameter(None))
        self.assertEqual(3, solution.diameter(root))
