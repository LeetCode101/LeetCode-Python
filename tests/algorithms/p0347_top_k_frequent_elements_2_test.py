import unittest
from leetcode.algorithms.p0347_top_k_frequent_elements_2 import Solution


class TestTopKFrequentElements(unittest.TestCase):
    def test_top_k_frequent_elements(self):
        solution = Solution()

        self.assertListEqual([1, 2], solution.topKFrequent(
            [1, 1, 1, 2, 2, 3], 2))
        self.assertListEqual([1], solution.topKFrequent([1], 1))
