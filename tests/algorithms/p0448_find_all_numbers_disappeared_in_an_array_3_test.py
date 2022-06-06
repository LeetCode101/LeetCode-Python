import unittest
from leetcode.algorithms.p0448_find_all_numbers_disappeared_in_an_array_3 \
    import Solution


class TestFindAllNumbersDisappearedInAnArray(unittest.TestCase):
    def test_find_all_numbers_disappeared_in_an_array(self):
        solution = Solution()

        self.assertListEqual([5, 6], solution.findDisappearedNumbers(
            [4, 3, 2, 7, 8, 2, 3, 1]))
