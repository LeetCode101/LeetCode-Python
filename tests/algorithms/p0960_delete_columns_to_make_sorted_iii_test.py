import unittest
from leetcode.algorithms.p0960_delete_columns_to_make_sorted_iii \
    import Solution


class TestDeleteColumnsToMakeSorted(unittest.TestCase):
    def test_delete_columns_to_make_sorted(self):
        solution = Solution()

        self.assertEqual(3, solution.minDeletionSize(['babca', 'bbazb']))
        self.assertEqual(4, solution.minDeletionSize(['edcba']))
        self.assertEqual(0, solution.minDeletionSize(['ghi', 'def', 'abc']))
