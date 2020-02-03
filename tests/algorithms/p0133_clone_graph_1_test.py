import unittest
from leetcode.algorithms.p0133_clone_graph_1 import Solution, Node


class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        solution = Solution()
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.neighbors = [b, d]
        b.neighbors = [a, c]
        c.neighbors = [b, d]
        d.neighbors = [a, c]

        self.assertIsNone(solution.cloneGraph(None))
        self.assertEqual(1, solution.cloneGraph(a).val)
