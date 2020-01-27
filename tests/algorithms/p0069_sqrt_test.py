import unittest
from leetcode.algorithms.p0069_sqrt import Solution


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        solution = Solution()

        self.assertEqual(2, solution.mySqrt(4))
        self.assertEqual(2, solution.mySqrt(8))
