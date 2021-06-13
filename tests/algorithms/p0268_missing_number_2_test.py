import unittest
from leetcode.algorithms.p0268_missing_number_2 import Solution


class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        solution = Solution()

        self.assertEqual(2, solution.missingNumber([3, 0, 1]))
        self.assertEqual(8, solution.missingNumber(
            [9, 6, 4, 2, 3, 5, 7, 0, 1]))
