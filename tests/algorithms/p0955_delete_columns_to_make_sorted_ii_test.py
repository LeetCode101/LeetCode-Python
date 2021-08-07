import unittest
from leetcode.algorithms.p0955_delete_columns_to_make_sorted_ii import Solution


class TestDeleteColumnsToMakeSorted(unittest.TestCase):
    def test_delete_columns_to_make_sorted(self):
        solution = Solution()

        self.assertEqual(1, solution.minDeletionSize(['ca', 'bb', 'ac']))
        self.assertEqual(3, solution.minDeletionSize(['zyx', 'wvu', 'tsr']))
