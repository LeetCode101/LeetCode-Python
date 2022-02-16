import unittest
from leetcode.algorithms.p1353_maximum_number_of_events_that_can_be_attended \
    import Solution


class TestMaximumNumberOfEventsThatCanBeAttended(unittest.TestCase):
    def test_maximum_number_of_events_that_can_be_attended(self):
        solution = Solution()

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
