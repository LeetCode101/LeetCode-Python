import unittest
from leetcode.algorithms.p0280_wiggle_sort_1 import Solution


class TestWiggleSort(unittest.TestCase):
    def test_wiggle_sort(self):
        solution = Solution()
        list1 = [3, 5, 2, 1, 6, 4]
        list2 = [6, 6, 5, 6, 3, 8]

        solution.wiggleSort(list1)
        solution.wiggleSort(list2)

        self.assertListEqual([1, 3, 2, 5, 4, 6], list1)
        self.assertListEqual([3, 6, 5, 6, 6, 8], list2)
