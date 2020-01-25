import unittest
from leetcode.algorithms.p0230_kth_smallest_element_in_a_bst_1 \
    import Solution, TreeNode


class TestKthSmallestElementInABST(unittest.TestCase):
    def test_kth_smallest_element_in_a_bst(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(1)
        c = TreeNode(4)
        d = TreeNode(2)
        a.left = b
        a.right = c
        b.right = d

        self.assertEqual(1, solution.kthSmallest(a, 1))
