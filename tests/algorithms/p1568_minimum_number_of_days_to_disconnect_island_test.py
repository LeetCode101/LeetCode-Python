import unittest
from leetcode.algorithms.p1568_minimum_number_of_days_to_disconnect_island \
    import Solution


class TestMinimumNumberOfDaysToDisconnectIsland(unittest.TestCase):
    def test_minimum_number_of_days_to_disconnect_island(self):
        solution = Solution()

        self.assertEqual(0, solution.minDays([]))
        self.assertEqual(2, solution.minDays(
            [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
        self.assertEqual(0, solution.minDays([[1, 0], [0, 1]]))
        self.assertEqual(1, solution.minDays([[1, 0], [1, 1]]))
