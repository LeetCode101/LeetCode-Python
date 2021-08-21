import unittest
from leetcode.algorithms.p1712_ways_to_split_array_into_three_subarrays \
    import Solution


class TestWaysToSplitArrayIntoThreeSubarrays(unittest.TestCase):
    def test_ways_to_split_array_into_three_subarrays(self):
        solution = Solution()

        self.assertEqual(1, solution.waysToSplit([1, 1, 1]))
        self.assertEqual(3, solution.waysToSplit([1, 2, 2, 2, 5, 0]))
        self.assertEqual(0, solution.waysToSplit([3, 2, 1]))
