import unittest
from leetcode.algorithms.p2007_find_original_array_from_doubled_array \
    import Solution


class TestFindOriginalArrayFromDoubledArray(unittest.TestCase):
    def test_find_original_array_from_doubled_array(self):
        solution = Solution()

        self.assertListEqual([1, 2, 2], solution.findOriginalArray(
            [2, 1, 2, 4, 2, 4]))
        self.assertListEqual([0, 0], solution.findOriginalArray([0] * 4))
        self.assertListEqual([], solution.findOriginalArray([6, 3, 0, 1]))
        self.assertListEqual([1, 3, 4], solution.findOriginalArray(
            [1, 3, 4, 2, 6, 8]))
