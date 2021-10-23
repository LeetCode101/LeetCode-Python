import unittest
from leetcode.algorithms.p0582_kill_process_2 import Solution


class TestKillProcess(unittest.TestCase):
    def test_kill_process(self):
        solution = Solution()

        self.assertListEqual([1, 3, 5, 4, 2], solution.killProcess(
            [1, 2, 3, 4, 5], [0, 1, 1, 3, 3], 1))
        self.assertListEqual([5, 10], solution.killProcess(
            [1, 3, 10, 5], [3, 0, 5, 3], 5))
