import unittest
from leetcode.algorithms.p0442_find_all_duplicates_in_an_array_2 \
    import Solution


class TestFindAllDuplicatesInAnArray(unittest.TestCase):
    def test_find_all_duplicates_in_an_array(self):
        solution = Solution()

        self.assertListEqual([2, 3], solution.findDuplicates(
            [4, 3, 2, 7, 8, 2, 3, 1]))
        self.assertListEqual([1], solution.findDuplicates([1, 1, 2]))
