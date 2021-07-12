import unittest
from leetcode.algorithms.p1658_minimum_operations_to_reduce_x_to_zero_1 \
    import Solution


class TestMinimumOperationsToReduceXToZero(unittest.TestCase):
    def test_minimum_operations_to_reduce_x_to_zero(self):
        solution = Solution()

        self.assertEqual(1, solution.minOperations([1], 1))
        self.assertEqual(2, solution.minOperations([1, 1, 4, 2, 3], 5))
        self.assertEqual(-1, solution.minOperations([5, 6, 7, 8, 9], 4))
