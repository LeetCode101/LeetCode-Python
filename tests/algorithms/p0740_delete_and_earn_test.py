import unittest
from leetcode.algorithms.p0740_delete_and_earn import Solution


class TestDeleteAndEarn(unittest.TestCase):
    def test_delete_and_earn(self):
        solution = Solution()

        self.assertEqual(6, solution.deleteAndEarn([3, 4, 2]))
        self.assertEqual(9, solution.deleteAndEarn([2, 2, 3, 3, 3, 4]))
