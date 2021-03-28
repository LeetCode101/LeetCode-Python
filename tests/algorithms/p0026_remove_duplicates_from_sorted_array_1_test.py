import unittest
from leetcode.algorithms\
    .p0026_remove_duplicates_from_sorted_array_1 import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_remove_duplicates_from_sorted_array(self):
        solution = Solution()

        self.assertEqual(2, solution.removeDuplicates([1, 1, 2]))
        self.assertEqual(
            5, solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
