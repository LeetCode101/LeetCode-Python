import unittest
from leetcode.algorithms.p0747_largest_number_at_least_twice_of_others_1 \
    import Solution


class TestLargestNumberAtLeastTwiceOfOthers(unittest.TestCase):
    def test_largest_number_at_least_twice_of_others(self):
        solution = Solution()

        self.assertEqual(-1, solution.dominantIndex([]))
        self.assertEqual(1, solution.dominantIndex([3, 6, 1, 0]))
        self.assertEqual(-1, solution.dominantIndex([1, 2, 3, 4]))
