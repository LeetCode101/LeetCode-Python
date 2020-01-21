import unittest
from leetcode.algorithms.p0189_rotate_array_1 import Solution


class TestRotateArray(unittest.TestCase):
    def test_rotate_array(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        solution.rotate(nums, 3)

        self.assertListEqual([5, 6, 7, 1, 2, 3, 4], nums)
