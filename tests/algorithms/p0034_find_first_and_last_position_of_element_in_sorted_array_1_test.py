import unittest
from leetcode.algorithms\
    .p0034_find_first_and_last_position_of_element_in_sorted_array_1 \
    import Solution


class TestFindFirstAndLastPositionOfElementInSortedArray(unittest.TestCase):
    def test_find_first_and_last_position_of_element_in_sorted_array(self):
        solution = Solution()

        self.assertListEqual([3, 4], solution.searchRange(
            [5, 7, 7, 8, 8, 10], 8))
        self.assertListEqual([-1, -1], solution.searchRange(
            [5, 7, 7, 8, 8, 10], 6))
