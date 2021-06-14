import unittest
from leetcode.algorithms.p0528_random_pick_with_weight import Solution


class TestRandomPickWithWeight(unittest.TestCase):
    def test_random_pick_with_weight(self):
        solution = Solution([1, 3])

        self.assertTrue(solution.pickIndex() in [0, 1])
