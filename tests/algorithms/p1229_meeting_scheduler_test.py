import unittest
from leetcode.algorithms.p1229_meeting_scheduler import Solution


class TestMeetingScheduler(unittest.TestCase):
    def test_meeting_scheduler(self):
        solution = Solution()

        self.assertListEqual([60, 68], solution.minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
        self.assertListEqual([], solution.minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
