import unittest
from leetcode.algorithms.p1636_sort_array_by_increasing_frequency_2 \
    import Solution


class TestSortArrayByIncreasingFrequency(unittest.TestCase):
    def test_sort_array_by_increasing_frequency(self):
        solution = Solution()

        self.assertListEqual([3, 1, 1, 2, 2, 2], solution.frequencySort(
            [1, 1, 2, 2, 2, 3]))
        self.assertListEqual([1, 3, 3, 2, 2], solution.frequencySort(
            [2, 3, 1, 3, 2]))
        self.assertListEqual(
            [5, -1, 4, 4, -6, -6, 1, 1, 1], solution.frequencySort(
                [-1, 1, -6, 4, 5, -6, 1, 4, 1]))
