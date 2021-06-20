import unittest
from leetcode.algorithms.p0759_employee_free_time import Solution, Interval


class TestEmployeeFreeTime(unittest.TestCase):
    def test_employee_free_time(self):
        solution = Solution()
        actual_list = solution.employeeFreeTime(
            [[Interval(1, 2), Interval(5, 6)],
             [Interval(1, 3)], [Interval(4, 10)]])

        self.assertListEqual([], solution.employeeFreeTime([]))
        self.assertListEqual([(3, 4)],
                             list(map(
                                 lambda x: (x.start, x.end), actual_list)))
