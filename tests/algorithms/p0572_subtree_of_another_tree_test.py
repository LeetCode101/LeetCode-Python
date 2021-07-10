import unittest
from leetcode.algorithms.p0572_subtree_of_another_tree \
    import Solution, TreeNode


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def test_subtree_of_another_tree(self):
        solution = Solution()
        root = TreeNode(
            3,
            TreeNode(4, TreeNode(1), TreeNode(2)),
            TreeNode(5)
        )
        sub_root = TreeNode(
            4,
            TreeNode(1),
            TreeNode(2)
        )

        self.assertTrue(solution.isSubtree(root, sub_root))
