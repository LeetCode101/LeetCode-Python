import unittest
from leetcode.algorithms\
    .p0632_smallest_range_covering_elements_from_k_lists_1 import Solution


class TestSmallestRangeCoveringElementsFromKLists(unittest.TestCase):
    def test_smallest_range_covering_elements_from_k_lists(self):
        solution = Solution()

        self.assertListEqual([20, 24], solution.smallestRange(
            [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
        self.assertListEqual([1, 1], solution.smallestRange(
            [[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
