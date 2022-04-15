import unittest
from leetcode.algorithms.p1430_check_if_a_string_ls_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree import \
    Solution, TreeNode  # noqa: E501


class TestCheckIfAStringIsAValidSequenceFromRootToLeavesPathInABinaryTree(
        unittest.TestCase):
    def test_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree(self):  # noqa: E501
        solution = Solution()
        root = TreeNode(
            0,
            TreeNode(1, TreeNode(0, None, TreeNode(1)),
                     TreeNode(1, TreeNode(0), TreeNode(0))),
            TreeNode(0, TreeNode(0))
        )

        self.assertTrue(solution.isValidSequence(root, [0, 1, 0, 1]))
        self.assertFalse(solution.isValidSequence(root, [1]))
