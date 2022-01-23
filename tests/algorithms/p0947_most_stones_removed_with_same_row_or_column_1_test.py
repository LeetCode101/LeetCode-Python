import unittest
from leetcode.algorithms.p0947_most_stones_removed_with_same_row_or_column_1 \
    import Solution


class TestMostStonesRemovedWithSameRowOrColumn(unittest.TestCase):
    def test_most_stones_removed_with_same_row_or_column(self):
        solution = Solution()

        self.assertEqual(5, solution.removeStones(
            [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
        self.assertEqual(3, solution.removeStones(
            [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
