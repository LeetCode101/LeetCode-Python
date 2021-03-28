import unittest
from leetcode.algorithms\
    .p0117_populating_next_right_pointers_in_each_node_ii_1 \
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
        g = Node(7)
        b.left = d
        b.right = e
        c.right = g
        solution.connect(a)

        self.assertEqual(b.next, c)
        self.assertEqual(d.next, e)
        self.assertEqual(e.next, g)
