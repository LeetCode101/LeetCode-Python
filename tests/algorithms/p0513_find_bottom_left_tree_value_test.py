import unittest
from leetcode.algorithms.p0513_find_bottom_left_tree_value \
    import Solution, TreeNode


class TestFindBottomLeftTreeValue(unittest.TestCase):
    def test_find_bottom_left_tree_value(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(
                3,
                TreeNode(5, TreeNode(7)),
                TreeNode(6)
            )
        )

        self.assertEqual(7, solution.findBottomLeftValue(root))
