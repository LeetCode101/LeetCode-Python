import unittest
from leetcode.algorithms.p0581_shortest_unsorted_continuous_subarray_2 \
    import Solution


class TestShortestUnsortedContinuousSubarray(unittest.TestCase):
    def test_shortest_unsorted_continuous_subarray(self):
        solution = Solution()

        self.assertEqual(5, solution.findUnsortedSubarray(
            [2, 6, 4, 8, 10, 9, 15]))
        self.assertEqual(0, solution.findUnsortedSubarray([1, 2, 3, 4]))
