import unittest
from leetcode.algorithms.p0791_custom_sort_string import Solution


class TestCustomSortString(unittest.TestCase):
    def test_custom_sort_string(self):
        solution = Solution()

        self.assertEqual('cbad', solution.customSortString('cba', 'abcd'))
        self.assertEqual('cbad', solution.customSortString('cbafg', 'abcd'))
