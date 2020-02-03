import unittest
from leetcode.algorithms.p0088_merge_sorted_array import Solution


class TestMergeSortedArray(unittest.TestCase):
    def test_merge_sorted_array(self):
        solution = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        actual_list = [1, 2, 2, 3, 5, 6]
        solution.merge(nums1, 3, nums2, 3)

        self.assertListEqual(actual_list, nums1)
