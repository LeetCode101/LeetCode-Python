import unittest
from leetcode.algorithms.p0719_find_kth_smallest_pair_distance import Solution


class TestFindKthSmallestPairDistance(unittest.TestCase):
    def test_find_kth_smallest_pair_distance(self):
        solution = Solution()

        self.assertEqual(0, solution.smallestDistancePair([1, 3, 1], 1))
