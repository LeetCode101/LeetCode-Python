import unittest
from leetcode.algorithms.p0048_rotate_image import Solution


class TestRotateImage(unittest.TestCase):
    def test_rotate_image(self):
        solution = Solution()
        actual_lists = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_lists = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        solution.rotate(actual_lists)

        self.assertListEqual(expected_lists, actual_lists)
