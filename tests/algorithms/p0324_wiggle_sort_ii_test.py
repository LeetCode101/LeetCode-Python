import unittest
from leetcode.algorithms.p0324_wiggle_sort_ii import Solution


class TestWiggleSort(unittest.TestCase):
    def test_wiggle_sort(self):
        solution = Solution()
        list1 = [1, 5, 1, 1, 6, 4]
        list2 = [1, 3, 2, 2, 3, 1]

        solution.wiggleSort(list1)
        solution.wiggleSort(list2)

        self.assertListEqual([1, 6, 1, 5, 1, 4], list1)
        self.assertListEqual([2, 3, 1, 3, 1, 2], list2)
