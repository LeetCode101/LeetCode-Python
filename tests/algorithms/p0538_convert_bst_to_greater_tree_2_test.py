import unittest
from leetcode.algorithms.p0538_convert_bst_to_greater_tree_2 \
    import Solution, TreeNode


class TestConvertBSTToGreaterTree(unittest.TestCase):
    def test_convert_bst_to_greater_tree(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
            TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))
        )

        self.assertEqual(30, solution.convertBST(root).val)
