import unittest
from leetcode.algorithms\
    .p1963_minimum_number_of_swaps_to_make_the_string_balanced import Solution


class TestMinimumNumberOfSwapsToMakeTheStringBalanced(unittest.TestCase):
    def test_minimum_number_of_swaps_to_make_the_string_balanced(self):
        solution = Solution()

        self.assertEqual(1, solution.minSwaps('][]['))
        self.assertEqual(2, solution.minSwaps(']]][[['))
        self.assertEqual(0, solution.minSwaps('[]'))
