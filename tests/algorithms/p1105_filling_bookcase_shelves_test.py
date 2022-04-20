import unittest
from leetcode.algorithms.p1105_filling_bookcase_shelves import Solution


class TestFillingBookcaseShelves(unittest.TestCase):
    def test_filling_bookcase_shelves(self):
        solution = Solution()

        self.assertEqual(6, solution.minHeightShelves(
            [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
        self.assertEqual(4, solution.minHeightShelves(
            [[1, 3], [2, 4], [3, 2]], 6))
