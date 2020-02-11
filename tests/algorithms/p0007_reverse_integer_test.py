import unittest
from leetcode.algorithms.p0007_reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer(self):
        solution = Solution()

        self.assertEqual(321, solution.reverse(123))
        self.assertEqual(-321, solution.reverse(-123))
        self.assertEqual(0, solution.reverse(9999999999))
