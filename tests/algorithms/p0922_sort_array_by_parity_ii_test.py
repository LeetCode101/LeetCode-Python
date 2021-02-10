import unittest
from leetcode.algorithms.p0922_sort_array_by_parity_ii import Solution


class TestSortArrayByParity(unittest.TestCase):
    def test_sort_array_by_parity(self):
        solution = Solution()

        self.assertListEqual([4, 5, 2, 7], solution.sortArrayByParityII(
            [4, 2, 5, 7]))
        self.assertListEqual([4, 5, 2, 7], solution.sortArrayByParityII(
            [4, 5, 2, 7]))
