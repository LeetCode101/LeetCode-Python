import unittest
from leetcode.algorithms.p1462_course_schedule_iv import Solution


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        solution = Solution()

        self.assertListEqual([False, True], solution.checkIfPrerequisite(
            2, [[1, 0]], [[0, 1], [1, 0]]))
        self.assertListEqual([True, True], solution.checkIfPrerequisite(
            3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))
