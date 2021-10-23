import unittest
from leetcode.algorithms.p0582_kill_process import Solution


class TestKillProcess(unittest.TestCase):
    def test_kill_process(self):
        solution = Solution()


        self.assertListEqual([1, 2, 3], solution.killProcess(
            [1, 2, 3], [0, 1, 1], 1))
        self.assertListEqual([5, 10], solution.killProcess(
            [1, 3, 10, 5], [3, 0, 5, 3], 5))
