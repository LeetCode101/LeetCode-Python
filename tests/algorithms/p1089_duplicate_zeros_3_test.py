import unittest
from leetcode.algorithms.p1089_duplicate_zeros_3 import Solution


class TestDuplicateZeros(unittest.TestCase):
    def test_duplicate_zeros(self):
        solution = Solution()
        actual_list = [1, 0, 2, 3, 0, 4, 5, 0]
        expected_list = [1, 0, 0, 2, 3, 0, 0, 4]
        solution.duplicateZeros(actual_list)

        self.assertListEqual(expected_list, actual_list)
