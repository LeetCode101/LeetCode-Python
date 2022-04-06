import unittest
from leetcode.algorithms.p1296_divide_array_in_sets_of_k_consecutive_numbers \
    import Solution


class TestDivideArrayInSetsOfKConsecutiveNumbers(unittest.TestCase):
    def test_divide_array_in_sets_of_k_consecutive_numbers(self):
        solution = Solution()

        self.assertTrue(solution.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
        self.assertTrue(solution.isPossibleDivide(
            [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
        self.assertFalse(solution.isPossibleDivide([1, 2, 3, 4], 3))
