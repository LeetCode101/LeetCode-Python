import unittest
from leetcode.algorithms.p1110_delete_nodes_and_return_forest_3 \
    import Solution, TreeNode


class TestDeleteNodesAndReturnForest(unittest.TestCase):
    def test_delete_nodes_and_return_forest(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7))
        )

        self.assertListEqual([1, 6, 7], list(map(
            lambda x: x.val, solution.delNodes(root, [3, 5]))))
