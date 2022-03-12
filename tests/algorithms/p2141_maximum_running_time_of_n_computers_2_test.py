import unittest
from leetcode.algorithms.p2141_maximum_running_time_of_n_computers_2 \
    import Solution


class TestMaximumRunningTimeOfNComputers(unittest.TestCase):
    def test_maximum_running_time_of_n_computers(self):
        solution = Solution()

        self.assertEqual(8, solution.maxRunTime(3, [10, 10, 3, 5]))
        self.assertEqual(4, solution.maxRunTime(2, [3, 3, 3]))
        self.assertEqual(2, solution.maxRunTime(2, [1, 1, 1, 1]))
