import unittest
from leetcode.algorithms.p0528_random_pick_with_weight import Solution


class TestRandomPickWithWeight(unittest.TestCase):
    def test_random_pick_with_weight(self):
        solution1 = Solution([3, 14, 1, 7])
        solution2 = Solution([1, 3])

        self.assertTrue(solution1.pickIndex() in [0, 1, 2, 3])
        self.assertTrue(solution2.pickIndex() in [0, 1])
