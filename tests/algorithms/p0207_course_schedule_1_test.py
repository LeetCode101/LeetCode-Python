import unittest
from leetcode.algorithms.p0207_course_schedule_1 import Solution


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        solution = Solution()

        self.assertTrue(solution.canFinish(
            5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
        self.assertFalse(solution.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
        self.assertTrue(solution.canFinish(2, [[1, 0]]))
        self.assertFalse(solution.canFinish(2, [[1, 0], [0, 1]]))
