import unittest
from leetcode.algorithms.p0260_single_number_iii import Solution


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        solution = Solution()

        self.assertListEqual([3, 5], sorted(solution.singleNumber(
            [1, 2, 1, 3, 2, 5])))
