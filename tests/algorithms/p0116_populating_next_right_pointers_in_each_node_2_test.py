import unittest
from leetcode.algorithms.p0116_populating_next_right_pointers_in_each_node_2 \
    import Solution, Node


class TestPopulatingNextRightPointersInEachNode(unittest.TestCase):
    def test_populating_next_right_pointers_in_each_node(self):
        solution = Solution()
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.left = b
        a.right = c
        d = Node(4)
        e = Node(5)
        f = Node(6)
        g = Node(7)
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        solution.connect(a)

        self.assertEqual(b.next, c)
        self.assertEqual(d.next, e)
        self.assertEqual(e.next, f)
        self.assertEqual(f.next, g)
