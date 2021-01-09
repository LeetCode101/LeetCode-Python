import unittest
from leetcode.algorithms.p0080_remove_duplicates_from_sorted_array_ii \
    import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_remove_duplicates_from_sorted_array(self):
        solution = Solution()

        self.assertEqual(0, solution.removeDuplicates([]))
        self.assertEqual(
            7, solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
