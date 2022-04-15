import unittest
from leetcode.algorithms.p1315_sum_of_nodes_with_even_valued_grandparent \
    import Solution, TreeNode


class TestSumOfNodesWithEvenValuedGrandparent(unittest.TestCase):
    def test_sum_of_nodes_with_even_valued_grandparent(self):
        solution = Solution()
        root = TreeNode(
            6,
            TreeNode(7, TreeNode(2, TreeNode(9)),
                     TreeNode(7, TreeNode(1), TreeNode(4))),
            TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5)))
        )

        self.assertEqual(18, solution.sumEvenGrandparent(root))
