import unittest
from leetcode.algorithms\
    .p1353_maximum_number_of_events_that_can_be_attended_1 import Solution


class TestMaximumNumberOfEventsThatCanBeAttended(unittest.TestCase):
    def test_maximum_number_of_events_that_can_be_attended(self):
        solution = Solution()

        self.assertEqual(18, solution.maxEvents(
            [[27, 27], [8, 10], [9, 11], [20, 21], [25, 29], [17, 20],
             [12, 12], [12, 12], [10, 14], [7, 7], [6, 10],
             [7, 7], [4, 8], [30, 31], [23, 25], [4, 6], [17, 17],
             [13, 14], [6, 9], [13, 14]]))
        self.assertEqual(0, solution.maxEvents([]))
        self.assertEqual(4, solution.maxEvents(
            [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
        self.assertEqual(5, solution.maxEvents(
            [[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
        self.assertEqual(5, solution.maxEvents(
            [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]))
        self.assertEqual(3, solution.maxEvents([[1, 2], [2, 3], [3, 4]]))
        self.assertEqual(4, solution.maxEvents(
            [[1, 2], [2, 3], [3, 4], [1, 2]]))
        self.assertEqual(3, solution.maxEvents(
            [[1, 2], [1, 2], [1, 6], [1, 2], [1, 2]]))
