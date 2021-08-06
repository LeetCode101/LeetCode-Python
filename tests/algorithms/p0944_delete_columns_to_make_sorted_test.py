import unittest
from leetcode.algorithms.p0944_delete_columns_to_make_sorted import Solution


class TestDeleteColumnsToMakeSorted(unittest.TestCase):
    def test_delete_columns_to_make_sorted(self):
        solution = Solution()

        self.assertEqual(0, solution.minDeletionSize([]))
        self.assertEqual(1, solution.minDeletionSize(['cba', 'daf', 'ghi']))
        self.assertEqual(3, solution.minDeletionSize(['zyx', 'wvu', 'tsr']))
