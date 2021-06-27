import unittest
from leetcode.algorithms.p0011_container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    def test_container_with_most_water(self):
        solution = Solution()

        self.assertEqual(16, solution.maxArea([4, 3, 2, 1, 4]))
        self.assertEqual(2, solution.maxArea([1, 2, 3]))
