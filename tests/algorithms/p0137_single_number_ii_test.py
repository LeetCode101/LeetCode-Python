import unittest
from leetcode.algorithms.p0137_single_number_ii import Solution


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()

        self.assertEqual(99, solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))
