import unittest
from leetcode.algorithms.p2146_k_highest_ranked_items_within_a_price_range \
    import Solution


class TestKHighestRankedItemsWithinAPriceRange(unittest.TestCase):
    def test_k_highest_ranked_items_within_a_price_range(self):
        solution = Solution()

        self.assertListEqual([[0, 1], [1, 1], [2, 1]],
                             solution.highestRankedKItems(
            [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [2, 5], [0, 0], 3))
        self.assertListEqual([[2, 1], [1, 2]], solution.highestRankedKItems(
            [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]], [2, 3], [2, 3], 2))
        self.assertListEqual([[2, 1], [2, 0]], solution.highestRankedKItems(
            [[1, 1, 1], [0, 0, 1], [2, 3, 4]], [2, 3], [0, 0], 3))
