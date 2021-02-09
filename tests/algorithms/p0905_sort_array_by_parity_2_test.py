import unittest
from leetcode.algorithms.p0905_sort_array_by_parity_2 import Solution


class TestSortArrayByParity(unittest.TestCase):
    def test_sort_array_by_parity(self):
        solution = Solution()

        self.assertListEqual([4, 2, 1, 3], solution.sortArrayByParity(
            [3, 1, 2, 4]))
        self.assertListEqual([4, 2, 1, 3], solution.sortArrayByParity(
            [4, 2, 1, 3]))
