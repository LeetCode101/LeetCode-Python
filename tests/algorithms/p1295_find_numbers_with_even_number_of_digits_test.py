import unittest
from leetcode.algorithms.p1295_find_numbers_with_even_number_of_digits \
    import Solution


class TestFindNumbersWithEvenNumberOfDigits(unittest.TestCase):
    def test_find_numbers_with_even_number_of_digits(self):
        solution = Solution()

        self.assertEqual(2, solution.findNumbers([12, 345, 2, 6, 7896]))
