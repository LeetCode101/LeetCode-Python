import unittest
from leetcode.algorithms.p0510_inorder_successor_in_bst_ii \
    import Solution, Node


class TestInorderSuccessorInBST(unittest.TestCase):
    def test_inorder_successor_in_bst(self):
        solution = Solution()
        a = Node(5)
        b = Node(3)
        c = Node(6)
        a.left = b
        a.right = c
        b.parent = a
        c.parent = a
        d = Node(2)
        e = Node(4)
        b.left = d
        b.right = e
        d.parent = b
        e.parent = b
        f = Node(1)
        d.left = f
        f.parent = d

        o = Node(1)
        p = Node(2)
        q = Node(3)
        o.right = p
        p.parent = o
        p.left = q
        q.parent = p

        self.assertEqual(5, solution.inorderSuccessor(e).val)
        self.assertIsNone(solution.inorderSuccessor(c))
        self.assertEqual(4, solution.inorderSuccessor(b).val)
        self.assertEqual(3, solution.inorderSuccessor(o).val)
