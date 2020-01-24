import unittest
from leetcode.algorithms.p0259_3sum_smaller import Solution


class Test3SumSmaller(unittest.TestCase):
    def test_3sum_smaller(self):
        solution = Solution()

        self.assertEqual(2, solution.threeSumSmaller([-2, 0, 1, 3], 2))
