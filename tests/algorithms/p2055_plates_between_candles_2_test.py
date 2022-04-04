import unittest
from leetcode.algorithms.p2055_plates_between_candles_2 import Solution


class TestPlatesBetweenCandles(unittest.TestCase):
    def test_plates_between_candles(self):
        solution = Solution()

        self.assertListEqual([2, 3], solution.platesBetweenCandles(
            '**|**|***|', [[2, 5], [5, 9]]))
        self.assertListEqual([9, 0, 0, 0, 0], solution.platesBetweenCandles(
            '***|**|*****|**||**|*',
            [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
