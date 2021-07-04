import unittest
from leetcode.algorithms.p0630_course_schedule_iii import Solution


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        solution = Solution()

        self.assertEqual(3, solution.scheduleCourse(
            [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
        self.assertEqual(0, solution.scheduleCourse([[3, 2], [4, 3]]))
