import unittest
from leetcode.algorithms.p0954_array_of_doubled_pairs import Solution


class TestArrayOfDoubledPairs(unittest.TestCase):
    def test_array_of_doubled_pairs(self):
        solution = Solution()

        self.assertFalse(solution.canReorderDoubled([3, 1, 3, 6]))
        self.assertFalse(solution.canReorderDoubled([2, 1, 2, 6]))
        self.assertTrue(solution.canReorderDoubled([4, -2, 2, -4]))
