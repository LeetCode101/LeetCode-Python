import unittest
from leetcode.algorithms.p2196_create_binary_tree_from_descriptions \
    import Solution


class TestCreateBinaryTreeFromDescriptions(unittest.TestCase):
    def test_create_binary_tree_from_descriptions(self):
        solution = Solution()

        self.assertEqual(50, solution.createBinaryTree(
            [[20, 15, 1], [20, 17, 0], [50, 20, 1],
             [50, 80, 0], [80, 19, 1]]).val)
        self.assertEqual(1, solution.createBinaryTree(
            [[1, 2, 1], [2, 3, 0], [3, 4, 1]]).val)
