import unittest
from leetcode.algorithms.p0905_sort_array_by_parity_1 import Solution


class TestSortArrayByParity(unittest.TestCase):
    def test_sort_array_by_parity(self):
        solution = Solution()

        self.assertListEqual([2, 4, 3, 1], solution.sortArrayByParity(
            [3, 1, 2, 4]))
