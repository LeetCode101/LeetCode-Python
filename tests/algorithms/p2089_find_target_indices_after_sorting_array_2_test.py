import unittest
from leetcode.algorithms.p2089_find_target_indices_after_sorting_array_2 \
    import Solution


class TestFindTargetIndicesAfterSortingArray(unittest.TestCase):
    def test_find_target_indices_after_sorting_array(self):
        solution = Solution()

        self.assertListEqual([1, 2], solution.targetIndices(
            [1, 2, 5, 2, 3], 2))
        self.assertListEqual([3], solution.targetIndices([1, 2, 5, 2, 3], 3))
        self.assertListEqual([4], solution.targetIndices([1, 2, 5, 2, 3], 5))
