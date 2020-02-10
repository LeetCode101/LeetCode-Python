import unittest
from leetcode.algorithms.p0253_meeting_rooms_ii import Solution


class TestMeetingRooms(unittest.TestCase):
    def test_meeting_rooms(self):
        solution = Solution()

        self.assertEqual(0, solution.minMeetingRooms([]))
        self.assertEqual(
            2, solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(1, solution.minMeetingRooms([[7, 10], [2, 4]]))
