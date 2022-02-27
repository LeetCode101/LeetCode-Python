import unittest
from leetcode.algorithms.p0923_3_sum_with_multiplicity import Solution


class Test3SumWithMultiplicity(unittest.TestCase):
    def test_3_sum_with_multiplicity(self):
        solution = Solution()

        self.assertEqual(20, solution.threeSumMulti(
            [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
        self.assertEqual(12, solution.threeSumMulti([1, 1, 2, 2, 2, 2], 5))
