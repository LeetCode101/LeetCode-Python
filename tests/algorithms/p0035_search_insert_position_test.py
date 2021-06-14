import unittest
from leetcode.algorithms.p0035_search_insert_position import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert_position(self):
        solution = Solution()

        self.assertEqual(2, solution.searchInsert([1, 3, 5, 6], 5))
