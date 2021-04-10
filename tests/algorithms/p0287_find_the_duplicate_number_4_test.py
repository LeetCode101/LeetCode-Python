import unittest
from leetcode.algorithms.p0287_find_the_duplicate_number_4 import Solution


class TestFindTheDuplicateNumber(unittest.TestCase):
    def test_find_the_duplicate_number(self):
        solution = Solution()

        self.assertEqual(2, solution.findDuplicate([1, 3, 4, 2, 2]))
        self.assertEqual(3, solution.findDuplicate([3, 1, 3, 4, 2]))
