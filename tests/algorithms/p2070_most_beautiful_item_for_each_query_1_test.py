import unittest
from leetcode.algorithms.p2070_most_beautiful_item_for_each_query_1 \
    import Solution


class TestMostBeautifulItemForEachQuery(unittest.TestCase):
    def test_most_beautiful_item_for_each_query(self):
        solution = Solution()

        self.assertListEqual([2, 4, 5, 5, 6, 6], solution.maximumBeauty(
            [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
        self.assertListEqual([4], solution.maximumBeauty(
            [[1, 2], [1, 2], [1, 3], [1, 4]], [1]))
        self.assertListEqual([0], solution.maximumBeauty([[10, 1000]], [5]))
