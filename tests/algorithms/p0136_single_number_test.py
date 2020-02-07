import unittest
from leetcode.algorithms.p0136_single_number import Solution


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()

        self.assertEqual(1, solution.singleNumber([2, 2, 1]))
