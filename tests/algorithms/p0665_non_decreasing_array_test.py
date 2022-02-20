import unittest
from leetcode.algorithms.p0665_non_decreasing_array import Solution


class TestNonDecreasingArray(unittest.TestCase):
    def test_non_decreasing_array(self):
        solution = Solution()

        self.assertFalse(solution.checkPossibility([3, 4, 2, 3]))
        self.assertTrue(solution.checkPossibility([4, 2, 3]))
        self.assertFalse(solution.checkPossibility([4, 2, 1]))
