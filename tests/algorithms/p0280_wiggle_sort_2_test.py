import unittest
from leetcode.algorithms.p0280_wiggle_sort_2 import Solution


class TestWiggleSort(unittest.TestCase):
    def test_wiggle_sort(self):
        solution = Solution()
        list1 = [3, 5, 2, 1, 6, 4]
        list2 = [6, 6, 5, 6, 3, 8]

        solution.wiggleSort(list1)
        solution.wiggleSort(list2)

        self.assertListEqual([3, 5, 1, 6, 2, 4], list1)
        self.assertListEqual([6, 6, 5, 6, 3, 8], list2)
