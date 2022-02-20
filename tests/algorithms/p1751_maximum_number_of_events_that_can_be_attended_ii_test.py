import unittest
from leetcode.algorithms \
    .p1751_maximum_number_of_events_that_can_be_attended_ii import Solution


class TestMaximumNumberOfEventsThatCanBeAttended(unittest.TestCase):
    def test_maximum_number_of_events_that_can_be_attended(self):
        solution = Solution()

        self.assertEqual(7, solution.maxValue(
            [[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2))
        self.assertEqual(10, solution.maxValue(
            [[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2))
        self.assertEqual(9, solution.maxValue(
            [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3))
