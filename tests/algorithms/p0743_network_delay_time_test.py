import unittest
from leetcode.algorithms.p0743_network_delay_time import Solution


class TestNetworkDelayTime(unittest.TestCase):
    def test_network_delay_time(self):
        solution = Solution()

        self.assertEqual(3, solution.networkDelayTime(
            [[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1))
        self.assertEqual(2, solution.networkDelayTime(
            [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
        self.assertEqual(1, solution.networkDelayTime([[1, 2, 1]], 2, 1))
        self.assertEqual(-1, solution.networkDelayTime([[1, 2, 1]], 2, 2))
