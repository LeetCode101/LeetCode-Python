import unittest
from leetcode.algorithms.p0652_find_duplicate_subtrees \
    import Solution, TreeNode


class TestFindDuplicateSubtrees(unittest.TestCase):
    def test_find_duplicate_subtrees(self):
        solution = Solution()
        a = TreeNode(1)
        b = TreeNode(2, TreeNode(4))
        c = TreeNode(3)
        d = TreeNode(2, TreeNode(4))
        e = TreeNode(4)
        a.left = b
        a.right = c
        c.left = d
        c.right = e

        self.assertListEqual([2, 4], sorted(list(map(
            lambda x: x.val, solution.findDuplicateSubtrees(a)))))
