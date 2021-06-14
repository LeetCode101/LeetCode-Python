import unittest
from leetcode.algorithms.p01235_maximum_profit_in_job_scheduling \
    import Solution


class TestMaximumProfitInJobScheduling(unittest.TestCase):
    def test_maximum_profit_in_job_scheduling(self):
        solution = Solution()

        self.assertEqual(120, solution.jobScheduling(
            [1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
