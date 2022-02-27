import unittest
from leetcode.algorithms\
    .p1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number \
    import Solution


class TestMinimumAdjacentSwapsToReachTheKthSmallestNumber(unittest.TestCase):
    def test_minimum_adjacent_swaps_to_reach_the_kth_smallest_number(self):
        solution = Solution()

        self.assertEqual(2, solution.getMinSwaps('5489355142', 4))
        self.assertEqual(4, solution.getMinSwaps('11112', 4))
        self.assertEqual(3, solution.getMinSwaps('321', 1))
