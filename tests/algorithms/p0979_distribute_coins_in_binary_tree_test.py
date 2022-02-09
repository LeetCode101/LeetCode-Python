import unittest
from leetcode.algorithms.p0979_distribute_coins_in_binary_tree \
    import Solution, TreeNode


class TestDistributeCoinsInBinaryTree(unittest.TestCase):
    def test_distribute_coins_in_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            0,
            TreeNode(3),
            TreeNode(0)
        )

        self.assertEqual(3, solution.distributeCoins(root))
