import unittest
from leetcode.algorithms.p0941_valid_mountain_array_1 import Solution


class TestValidMountainArray(unittest.TestCase):
    def test_valid_mountain_array(self):
        solution = Solution()

        self.assertFalse(solution.validMountainArray([2, 1]))
        self.assertTrue(solution.validMountainArray([0, 3, 2, 1]))
        self.assertFalse(solution.validMountainArray([0, 1, 2, 3, 2, 5]))
