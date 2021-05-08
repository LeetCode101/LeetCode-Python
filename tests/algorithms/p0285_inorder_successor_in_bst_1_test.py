import unittest
from leetcode.algorithms.p0285_inorder_successor_in_bst_1 \
    import Solution, TreeNode


class TestInorderSuccessorInBST(unittest.TestCase):
    def test_inorder_successor_in_bst(self):
        solution = Solution()
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        a.left = b
        a.right = c
        d = TreeNode(2)
        e = TreeNode(4)
        b.left = d
        b.right = e
        e.left = TreeNode(1)

        self.assertEqual(5, solution.inorderSuccessor(a, e).val)
        self.assertIsNone(solution.inorderSuccessor(a, c))
