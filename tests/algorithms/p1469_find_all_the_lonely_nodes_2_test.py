import unittest
from leetcode.algorithms.p1469_find_all_the_lonely_nodes_2 \
    import Solution, TreeNode


class TestFindAllTheLonelyNodes(unittest.TestCase):
    def test_find_all_the_lonely_nodes(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, None, TreeNode(4)),
            TreeNode(3)
        )

        self.assertListEqual([], solution.getLonelyNodes(None))
        self.assertListEqual([4], solution.getLonelyNodes(root1))
