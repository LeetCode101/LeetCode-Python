import unittest
from leetcode.algorithms.p0575_distribute_candies import Solution


class TestDistributeCandies(unittest.TestCase):
    def test_distribute_candies(self):
        solution = Solution()

        self.assertEqual(3, solution.distributeCandies([1, 1, 2, 2, 3, 3]))
        self.assertEqual(2, solution.distributeCandies([1, 1, 2, 3]))
