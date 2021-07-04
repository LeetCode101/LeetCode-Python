import unittest
from leetcode.algorithms.p0210_course_schedule_ii_1 import Solution


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        solution = Solution()

        self.assertListEqual([], solution.findOrder(2, [[1, 0], [0, 1]]))
        self.assertListEqual([0, 1], solution.findOrder(2, [[1, 0]]))
        self.assertListEqual([0, 1, 2, 3], solution.findOrder(
            4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
