import unittest
from leetcode.algorithms \
    .p1481_least_number_of_unique_integers_after_k_removals import Solution


class TestLeastNumberOfUniqueIntegersAfterKRemovals(unittest.TestCase):
    def test_least_number_of_unique_integers_after_k_removals(self):
        solution = Solution()

        self.assertEqual(2, solution.findLeastNumOfUniqueInts(
            [4, 3, 1, 1, 3, 3, 2], 3))
        self.assertEqual(1, solution.findLeastNumOfUniqueInts([5, 5, 4], 1))
