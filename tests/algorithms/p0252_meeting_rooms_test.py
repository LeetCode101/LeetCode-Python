import unittest
from leetcode.algorithms.p0252_meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def test_meeting_rooms(self):
        solution = Solution()

        self.assertFalse(solution.canAttendMeetings(
            [[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(solution.canAttendMeetings([[7, 10], [2, 4]]))
