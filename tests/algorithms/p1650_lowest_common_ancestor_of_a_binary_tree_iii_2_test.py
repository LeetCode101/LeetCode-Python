import unittest
from leetcode.algorithms.p1650_lowest_common_ancestor_of_a_binary_tree_iii_2 \
    import Solution, Node


class TestLowestCommonAncestorOfABinaryTree(unittest.TestCase):
    def test_lowest_common_ancestor_of_a_binary_tree(self):
        solution = Solution()
        a = Node(3)
        b = Node(5)
        c = Node(1)
        a.left = b
        a.right = c
        b.parent = a
        c.parent = a
        d = Node(6)
        e = Node(2)
        b.left = d
        b.right = e
        d.parent = b
        e.parent = b
        f = Node(0)
        g = Node(8)
        c.left = f
        c.right = g
        f.parent = c
        g.parent = c
        h = Node(7)
        i = Node(4)
        e.left = h
        e.right = i
        h.parent = e
        i.parent = e

        self.assertEqual(3, solution.lowestCommonAncestor(b, c).val)
