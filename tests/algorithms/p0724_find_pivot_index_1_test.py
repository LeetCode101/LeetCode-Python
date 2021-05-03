import unittest
from leetcode.algorithms.p0724_find_pivot_index_1 import Solution


class TestFindPivotIndex(unittest.TestCase):
    def test_find_pivot_index(self):
        solution = Solution()

        self.assertEqual(-1, solution.pivotIndex([]))
        self.assertEqual(3, solution.pivotIndex([1, 7, 3, 6, 5, 6]))
        self.assertEqual(-1, solution.pivotIndex([1, 2, 3]))
