import unittest
from leetcode.algorithms.p0137_single_number_ii import Solution


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()

        self.assertEqual(99, solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))
        self.assertEqual(-4, solution.singleNumber(
            [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
