import unittest
from leetcode.algorithms.p0621_task_scheduler import Solution


class TestTaskScheduler(unittest.TestCase):
    def test_task_scheduler(self):
        solution = Solution()

        self.assertEqual(8, solution.leastInterval(
            ['A', 'A', 'A', 'B', 'B', 'B'], 2))
        self.assertEqual(6, solution.leastInterval(
            ['A', 'A', 'A', 'B', 'B', 'B'], 0))
        self.assertEqual(16, solution.leastInterval(
            ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2))
