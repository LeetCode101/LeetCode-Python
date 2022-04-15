import unittest
from leetcode.algorithms\
    .p2096_step_by_step_directions_from_a_binary_tree_node_to_another \
    import Solution, TreeNode


class TestStepByStepDirectionsFromABinaryTreeNodeToAnother(unittest.TestCase):
    def test_step_by_step_directions_from_a_binary_tree_node_to_another(self):
        solution = Solution()
        root = TreeNode(
            5,
            TreeNode(1, TreeNode(3)),
            TreeNode(2, TreeNode(6), TreeNode(4))
        )

        self.assertEqual('UURL', solution.getDirections(root, 3, 6))
        self.assertEqual('', solution.getDirections(TreeNode(1), 9, 9))
